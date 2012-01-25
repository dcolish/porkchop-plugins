"""
To use create a config in your porkchop conf dir called jsondata.ini. In that
config place the following::

   [jsondata]
   path = <path to your json file>

"""

import json

from porkchop.plugin import PorkchopPlugin, test_plugin_data


class JsondataPlugin(PorkchopPlugin):
    def get_data(self):
        try:
            path = self.config['jsondata']['path']
        except KeyError:
            return {}
        with open(path) as f:
            return json.load(f)

if __name__ == '__main__':
    print test_plugin_data('jsondata')
