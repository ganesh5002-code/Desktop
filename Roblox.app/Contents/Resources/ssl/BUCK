load("@roblox//:glob.bzl", "subdir_glob")
load("@roblox//:header_groups.bzl", "rbx_header_group", "make_header_map")

export_file(
    name="cacert.pem",
    visibility=["//..."],
    src="cacert.pem",
)

rbx_header_group(
    name="cacert_include",
    visibility=["//..."],
    header_map=subdir_glob([
        ("", "cacert.pem"),
    ]),
)
