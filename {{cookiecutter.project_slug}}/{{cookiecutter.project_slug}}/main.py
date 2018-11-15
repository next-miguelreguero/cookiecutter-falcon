# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
import os
# Third-party imports
import falcon



if os.getenv("FALCON_SETTINGS_MODULE") is None:
    os.environ["FALCON_SETTINGS_MODULE"] = "settings.local"

# Local imports
from {{ cookiecutter.project_slug }}.api.app import application

app = application

# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
