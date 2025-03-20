import os
import sys
import argparse
import logging
from time import strftime, localtime


DEFAULT_SCREENSHOT_LOCATION = os.environ.get("USERPROFILE") + "\\Pictures\\Screenshots"
DEFAULT_LOGGING_DIRECTORY = os.environ.get("HOMEDRIVE") + "\\Screenshot Organizer\\Log"
DEFAULT_LOGGING_FILE = os.environ.get("HOMEDRIVE") + "\\Screenshot Organizer\\Log\\log.log"

logger = logging.getLogger(__name__)

if not os.path.exists(DEFAULT_LOGGING_DIRECTORY):
    os.makedirs(DEFAULT_LOGGING_DIRECTORY)

logging.basicConfig(filename=DEFAULT_LOGGING_FILE, level=logging.INFO)

def get_last_file_modified(path):
    stat = os.path.getmtime(path)
    modified_time = strftime('%Y-%m', localtime(stat))
    return modified_time

def main():
    description = """Screenshot Organizer - Looks at the default location for Windows screenshots and organizes them by the year and month that the screenshot was taken. """
    path_help = "Specify the path to the screenshots folder. Default location is " + DEFAULT_SCREENSHOT_LOCATION
    parser=argparse.ArgumentParser(description=description)
    
    # ARGUMENTS
    parser.add_argument('-p', '--path', default=DEFAULT_SCREENSHOT_LOCATION, required=False, help=path_help)
    
    args = parser.parse_args()
    if args.path != DEFAULT_SCREENSHOT_LOCATION:
        path = sys.argv[2]
    else:
        path = DEFAULT_SCREENSHOT_LOCATION
    
    logging.info('Setting path to  %s', path)
    
    if not os.path.exists(path):
        logging.warning("Path doesn't exist. Try again with the correct path")
        sys.exit()

    for file in os.scandir(path):
        if file.is_file():
            source = file.path
            last_modified = get_last_file_modified(file.path)
            year = last_modified[0:4]
            month = last_modified[5:]
            year_dir = path + "\\" + year
            month_dir = year_dir + "\\" + month
            
            if not os.path.exists(year_dir):
                logger.info("Created a directory at {}", year_dir)
                os.mkdir(year_dir)

            if not os.path.exists(month_dir):
                logger.info("Created a directory at {}", month_dir)
                os.mkdir(month_dir)
            
            destination = month_dir + "\\" + file.name
            
            os.replace(file.path, destination)
            logger.info("Moved %s to %s", source, destination)

if __name__ == '__main__':
    main()