import os
import platform

OPERATING_SYSTEM = platform.system()

switch(OPERATING_SYSTEM):
    case 'Windows':
        DEFAULT_SCREENSHOT_LOCATION = os.environ.get(
            "USERPROFILE") + "\\Pictures\\Screenshots"
        DEFAULT_LOGGING_DIRECTORY = os.environ.get(
            "HOMEDRIVE") + "\\Screenshot Organizer\\Log"
        DEFAULT_LOGGING_FILE = os.environ.get(
            "HOMEDRIVE") + "\\Screenshot Organizer\\Log\\log.log"
    case 'Darwin':
        DEFAULT_SCREENSHOT_LOCATION =
        DEFAULT_LOGGING_DIRECTORY =
        DEFAULT_LOGGING_FILE =

    case 'Linux':
        DEFAULT_SCREENSHOT_LOCATION =
        DEFAULT_LOGGING_DIRECTORY =
        DEFAULT_LOGGING_FILE =
    case _:
        print("Unable to Detect OS")
