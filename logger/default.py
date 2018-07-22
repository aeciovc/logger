'''Logger: Log activities with support custom formats and remote stores'''

import logging
import logging.config
import json
import os

path_exec = os.path.dirname(os.path.abspath(__file__))

# usgin default logger config file
with open(os.path.join(path_exec, "logger.json"), "r", encoding="utf-8") as fd:
    logging.config.dictConfig(json.load(fd))

#Default file log
logger = logging.getLogger()
logger.name = "root.service"