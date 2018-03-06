from cx_Freeze import setup, Executable

base = None

includefiles = ['geckodriver.exe','readme.md','license.txt']
executables = [Executable("checkalerts.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "checkalerts",
    options = {'build_exe': {'include_files':includefiles}},
    version = "1.0",
    description = 'Checking alerts on Sophos Central.',
    executables = executables
)