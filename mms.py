"""
If you like add a mms.ini to your conf dir and define::

[mmstats]
path = <some path>

You can also run this as a standalone module for testing

"""

import glob
import os.path
from tempfile import tempdir

from mmstats.reader import MmStatsReader

from porkchop.plugin import PorkchopPlugin, PorkchopPluginHandler
from porkchop.util import parse_config


def iter_stats(glob_):
    """Yields a label at a time from every mmstats file in MMSTATS_DIR"""
    for fn in glob.glob(glob_):
        try:
            for label, value in MmStatsReader.from_mmap(fn):
                yield fn, label, value
        except Exception:
            continue


class MmsPlugin(PorkchopPlugin):

    def get_data(self):
        try:
            path = self.config['mmstats']['mmstats_path']
        except KeyError:
            path = tempdir()
        GLOB = os.path.join(path, 'mmstats-*')
        stats = {}
        for _, label, value in iter_stats(GLOB):
            stats.update({label: value})
        return stats

if __name__ == '__main__':
    plug = PorkchopPluginHandler('')
    mms = plug.plugins['mms']()
    mms.config = parse_config(mms.config_file)
    print mms.get_data()
