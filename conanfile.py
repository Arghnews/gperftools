from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment

import os

class GperftoolsConan(ConanFile):
    name = "gperftools"
    version = "0.1.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Gperftools here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        pass
        #  self.run("git clone https://github.com/conan-io/hello.git")
        #  # This small hack might be useful to guarantee proper /MT /MD linkage
        #  # in MSVC if the packaged project doesn't have variables to set it
        #  # properly
        #  tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
                              #  '''PROJECT(HelloWorld)
#  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#  conan_basic_setup()''')

    def build(self):
        #  cmake = CMake(self)
        #  cmake.configure(source_folder="hello")
        #  cmake.build()
        #  os.chdir("source_subfolder")
        autotools = AutoToolsBuildEnvironment(self)
        self.run("./autogen.sh")
        autotools.configure()
        autotools.make()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    #  def test(self):
        #  # Run test_package example program with CPUPROFILE=profile.prof
        #  # Should produce output file
        #  pass

    def package(self):
        #  os.chdir("source_subfolder")
        autotools = AutoToolsBuildEnvironment(self)
        autotools.install()
        #  self.copy("*.h", dst="include", src="hello")
        #  self.copy("*hello.lib", dst="lib", keep_path=False)
        #  self.copy("*.dll", dst="bin", keep_path=False)
        #  self.copy("*.so", dst="lib", keep_path=False)
        #  self.copy("*.dylib", dst="lib", keep_path=False)
        #  self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        # /usr/local/lib/libprofiler.a
        self.cpp_info.libs = ["profiler"]

