from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.files import collect_libs, copy, replace_in_file
from conan.tools.scm import Git


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
    default_options = {"shared": False}
    generators = ["CMakeDeps", "CMakeToolchain"]
    exports = ["LICENSE"]
    requires = (
        "libcurl/8.4.0",
        "jsoncpp/1.9.4"
    )


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def source(self):
        git = Git(self)
        git.clone(url=(self.homepage + ".git"), target=".")
        git.checkout(commit=self.version)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        copy(self, "LICENSE", ".", "licenses")

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
