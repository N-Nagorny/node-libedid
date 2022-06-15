#include <sstream>

#include <napi.h>

#include "edid/edid.hh"
#include "edid/exceptions.hh"

using namespace Napi;

static Napi::Value ParseEdidBinary(const CallbackInfo& info) {
  if (info.Length() != 1) {
    Napi::Error::New(info.Env(), "Expected exactly one argument")
        .ThrowAsJavaScriptException();
    return info.Env().Undefined();
  }
  if (!info[0].IsTypedArray()) {
    Napi::Error::New(info.Env(), "Expected a TypedArray")
        .ThrowAsJavaScriptException();
    return info.Env().Undefined();
  }

  Napi::Uint8Array arr = info[0].As<Napi::Uint8Array>();

  std::vector<uint8_t> edid_binary(arr.Data(), arr.Data() + arr.ByteLength() / sizeof(uint8_t));
  std::stringstream result;

  try {
    Edid::EdidData edid_data = Edid::parse_edid_binary(edid_binary);
    Edid::print_base_block(result, edid_data.base_block);
    if (edid_data.extension_blocks.has_value()) {
      for (const auto& block : edid_data.extension_blocks.value()) {
        Edid::print_cta861_block(result, block);
      }
    }
  } catch (const Edid::EdidException& e) {
    result << e.what();
  }

  return String::New(info.Env(), result.str());
}

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports["parseEdidBinary"] = Napi::Function::New(env, ParseEdidBinary);
  return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
