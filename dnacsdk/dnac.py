"""
Establish and manage connection to DNA Center.

This module (dnac.py) is designed to provide a "toolbox" of tools for interacting with the Cisco DNA Center API.
The "toolbox" is the DNAC class and the "tools" are its methods.  Note: There exists a "Quick Start Guide" for the Cisco
DNA Center API too.  Just Google for it as it gets updated with each release of code.
"""

import datetime
import requests
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
from logging.handlers import RotatingFileHandler
import warnings

# Disable annoying HTTP warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

""""
The 'requests' package is very chatty on the INFO logging level.  Change its logging threshold sent to logger to
something greater than INFO (i.e. not INFO or DEBUG) will cause it to not log its INFO and DEBUG messages to the
default logger.  This reduces the size of our log files.
"""
logging.getLogger("requests").setLevel(logging.WARNING)


class DNAC(object):
    """Establish and maintain connection to DNA Center."""

    pass
