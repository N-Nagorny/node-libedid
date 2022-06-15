{
	"variables": {
		"commit%":"6f4c8b543a75d7832a749b06af8700bd2b94a630",
	},
	"targets": [
		{
			"target_name": "action_before_build",
			"actions": [
				{
					"action_name": "clone_repo",
					"inputs": [],
					"outputs": [
						"libedid.tar.gz"
					],
					"action": ['wget', '-O', 'libedid.tar.gz', 'https://codeload.github.com/N-Nagorny/libedid/zip/<(commit)']
				},
				{
					"action_name": "unpack_src",
					"inputs": ['libedid.tar.gz'],
					"outputs": [
						"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/base_block.cc"
					],
					"action": ['unzip', '-o', 'libedid.tar.gz', '-d', '<(SHARED_INTERMEDIATE_DIR)']
				}
			]
		},
		{
			"target_name": "libedid",
			'type': 'static_library',
			"sources": [
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/base_block.cc",
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/common.cc",
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/edid.cc",
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/cta861_block.cc",
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/src/timing_modes.cc"
			],
			"cflags_cc!": [ "-fno-exceptions" ],
			"cflags_cc": [ "-std=c++17" ],
			"dependencies": [
				"action_before_build"
			],
			'include_dirs': [
				"<(SHARED_INTERMEDIATE_DIR)/libedid-<(commit)/include/"
			]
		}
	]
}
