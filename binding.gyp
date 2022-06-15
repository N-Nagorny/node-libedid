{
	"variables": {
		"commit%":"6f4c8b543a75d7832a749b06af8700bd2b94a630",
	},
	"targets" :[
		{
			"target_name": "edidparser",
			"sources": ["node-edid-parser.cc"],
			"cflags_cc!": [ "-fno-exceptions" ],
			"cflags_cc": [ "-std=c++17" ],
			"dependencies": [
				"deps/libedid.gyp:libedid"
			],
			'include_dirs': [
				"<!@(node -p \"require('node-addon-api').include\")",
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/include/"
			],
			"libraries": ["-Wl,-rpath,edid.a"],
		}
	]
}
