import os
import platform

OPERATING_SYSTEM = platform.system()

match(OPERATING_SYSTEM):
    case 'Windows':
        DEFAULT_SCREENSHOT_LOCATION = os.environ.get(
            "USERPROFILE") + "\\Pictures\\Screenshots"
        DEFAULT_LOGGING_DIRECTORY = os.environ.get(
            "HOMEDRIVE") + "\\Screenshot Organizer\\Log"
        DEFAULT_LOGGING_FILE = os.environ.get(
            "HOMEDRIVE") + "\\Screenshot Organizer\\Log\\log.log"
    case 'Darwin':
        DEFAULT_SCREENSHOT_LOCATION = os.environ.get("HOME") + "/Desktop"
        DEFAULT_LOGGING_DIRECTORY = '~/var/log/ScreenshotOrganizer'
        DEFAULT_LOGGING_FILE = '~/var/log/ScreenshotOrganizer/ScreenshotOrganizer.log'

    case _:
        print("Unable to Detect OS")
