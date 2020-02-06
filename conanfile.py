import os
from conans import ConanFile, tools


class WTLConan(ConanFile):
    name = "wtl"
    url = "https://github.com/bincrafters/conan-wtl"
    description = "Windows Template Library (WTL) is a C++ library for developing Windows applications and UI " \
                  "components. It extends ATL (Active Template Library) and provides a set of classes for controls, " \
                  "dialogs, frame windows, GDI objects, and more."
    homepage = "https://wtl.sourceforge.io"
    topics = ("template", "windows-template-library", "windows", "atl", "gdi")
    no_copy_source = True
    license = "Common Public License"
    exports = ["LICENSE.md"]
    settings = {'os': ['Windows']}

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])

    def package(self):
        self.copy(pattern="MS-PL.TXT", dst="license", src=self.source_folder)
        self.copy(pattern="*", dst="include", src=os.path.join(self.source_folder, "Include"))

    def package_id(self):
        self.info.header_only()
