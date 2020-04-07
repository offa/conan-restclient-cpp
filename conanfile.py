from conans import ConanFile, CMake, tools


class RestclientcppConan(ConanFile):
    name = "restclient-cpp"
    version = "0.5.2"
    license = "MIT"
    author = "offa <offa@github>"
    url = "https://github.com/offa/conan-restclient-cpp"
    description = "This is a simple REST client for C++. It wraps libcurl for HTTP requests."
    homepage = "https://github.com/mrtazz/restclient-cpp"
    topics = ("restclient", "libcurl", "rest-client", "http-client", "http")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake_find_package"
    exports = ["LICENSE"]
    _source_dir = "{}-{}".format(name, version)
    scm = {
        "type": "git",
        "subfolder": _source_dir,
        "url": "{}.git".format(homepage),
        "revision": version
    }
    requires = (
        "libcurl/7.64.1@bincrafters/stable",
        "jsoncpp/1.9.0@theirix/stable"
    )


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_dir, build_folder="build")
        return cmake

    def source(self):
        tools.replace_in_file("{}/CMakeLists.txt".format(self._source_dir), "CURL", "libcurl")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("LICENSE", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
