# encode = utf-8

"""
This module is used to filter and reload PATH.
This file is genrated by Splunk add-on builder
"""

import os
import sys
import re

if sys.version_info[0] < 3:
    py_version = "aob_py2"
else:
    py_version = "aob_py3"

ta_name = 'TA-splunk-add-on-for-datadog-api'
ta_lib_name = 'ta_splunk_add_on_for_datadog_api'
pattern = re.compile(r"[\\/]etc[\\/]apps[\\/][^\\/]+[\\/]bin[\\/]?$")
new_paths = [path for path in sys.path if not pattern.search(path) or ta_name in path]
new_paths.insert(0, os.path.sep.join([os.path.dirname(__file__), ta_lib_name]))
new_paths.insert(0, os.path.sep.join([os.path.dirname(__file__), ta_lib_name, py_version]))
sys.path = new_paths