# CheckAlerts

A python script to automatically check the alerts on Sophos Central console for you based on the description and severity. Currently, there isn't any filtering functionality by Sophos so until then, hopefully, this should be of use to you or your company!

## Prerequisites

I have only tested this on a Windows 10 x64 machine so far but It should work on any 64 bit Windows. (Please let me know if it doesn't)

Geckodriver.exe is required for Selenium automation to work. More info can be found here about Geckodriver https://github.com/mozilla/geckodriver

## Installing

### Easy Way (Pre-Compiled)

1. Download the .zip file on the release section https://github.com/0x6a6576/CheckAlerts/releases
2. Extract the .zip file

### Harder Way (Compile it yourself)

1. Download the source code
2. Extract the .zip file
3. Go to the extracted folder
4. Type "cmd" on the explorer URL bar and it should open cmd on the same directory
5. Run the command below
```
python setup.py build
```

## How to use the program

1. Open cmd and Change Dir(cd) to the directory where the checkalerts.exe is
2. Run the checkalerts with atleast a Severity and Description argument. List of all available arguments below:
..*-s/--severity (High, Medium or Info)
..*-d/--description (Description of the alert you want to clear ie. PUA, Malware etc.)
..*-u/--username (Your Sophos Central username - Optional)
..*-p/--password (Your Sophos Central password - Optional)
3. Watch the magic happen!

## Example
```
checkalerts -s medium -d pua -u mysopos@sophos.com -p myp@ssword111
```

## Built With

* [Selenium](http://www.seleniumhq.org/docs/) - Browser Automation
* [Python Standard Library](https://docs.python.org/3/library/index.html) - OS related stuff

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details