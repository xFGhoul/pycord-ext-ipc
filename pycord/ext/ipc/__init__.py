import collections

from pycord.ext.ipc.client import Client
from pycord.ext.ipc.server import Server
from pycord.ext.ipc.errors import *


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "2.1.1"
version_info = _VersionInfo(2, 1, 1, "final", 0)
