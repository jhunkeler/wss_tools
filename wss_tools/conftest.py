# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

from astropy.tests.pytest_plugins import *
import os

# Uncomment the following line to treat all DeprecationWarnings as
# exceptions
enable_deprecations_as_exceptions()

# Uncomment and customize the following lines to add/remove entries from
# the list of packages for which version numbers are displayed when running
# the tests. Making it pass for KeyError is essential in some cases when
# the package uses other astropy affiliated packages.
PYTEST_HEADER_MODULES['Astropy'] = 'astropy'
PYTEST_HEADER_MODULES['scikit-image'] = 'skimage'
del PYTEST_HEADER_MODULES['h5py']

# Uncomment the following lines to display the version number of the
# package rather than the version number of Astropy in the top line when
# running the tests.

# This is to figure out the affiliated package version, rather than
# using Astropy's
try:
    from .version import version
except ImportError:
    version = 'dev'

packagename = os.path.basename(os.path.dirname(__file__))
TESTED_VERSIONS[packagename] = version
