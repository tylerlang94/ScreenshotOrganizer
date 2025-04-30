import logging
import os

import globals


logger = logging.getLogger(__name__)

if not os.path.exists(globals.DEFAULT_LOGGING_DIRECTORY):
    os.makedirs(globals.DEFAULT_LOGGING_DIRECTORY)

logging.basicConfig(filename=globals.DEFAULT_LOGGING_FILE, level=logging.INFO)
