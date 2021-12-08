# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL module for InvenioRDM."""

from .ext import InvenioOCFL
from .version import __version__

__all__ = ('__version__', 'InvenioOCFL')
