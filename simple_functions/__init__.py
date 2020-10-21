"""initialization of testing according to lecture 7"""

from pkg_resources import get_distribution, DistributionNotFound
from .functions1 import * # noqa
from .constants import * # noqa

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
