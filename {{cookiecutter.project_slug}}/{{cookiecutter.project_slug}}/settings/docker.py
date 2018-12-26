# -*- coding: utf-8 -*-
"""
Docker settings file
"""
import os
# Local imports
# Third-party imports
from .base import *

DB = {"NAME": os.environ['DB_NAME'],
      "USERNAME": os.environ['DB_USERNAME'],
      "PASSWORD": os.environ['DB_PASSWORD'],
      "HOSTNAME": os.environ['DB_HOST'],
      "PORT": os.environ.get("DB_PORT", 5432)
}

