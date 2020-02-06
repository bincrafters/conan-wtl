from conans import ConanFile, tools


class WTLConan(ConanFile):
    name = "wtl"
    version = "10.0.9163"
    url = "https://github.com/bincrafters/conan-wtl"
    description = "Windows Template Library (WTL) is a C++ library for developing Windows applications and UI " \
                  "components. It extends ATL (Active Template Library) and provides a set of classes for controls, " \
                  "dialogs, frame windows, GDI objects, and more."
    no_copy_source = True
    license = "Common Public License"
    exports = ["LICENSE.md"]
    settings = {'os': ['Windows']}

    def source(self):
        major, _, build = self.version.split('.')
        source_url = "https://netcologne.dl.sourceforge.net/project/wtl/WTL%20{major}/WTL%20{version}/" \
                     "WTL{major}_{build}.zip".format(major=major, build=build, version=self.version)
        tools.get(source_url)

    def package(self):
        self.copy(pattern="MS-PL.TXT", dst="license", src=".")
        self.copy(pattern="*", dst="include", src="Include")

    def package_id(self):
        self.info.header_only()
