# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import setuptools

# Get version without import module
exec(compile(open('src/pk_core/version.py').read(),
             'pk_core/version.py', 'exec'))

setuptools.setup(
    version = __version__,
    package_dir = {
        '' : str('src')
    },
)
