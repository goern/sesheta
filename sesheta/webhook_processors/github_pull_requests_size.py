#!/usr/bin/env python3
# Sesheta
# Copyright(C) 2018 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This processes GitHub Pull Requests."""

import logging


import daiquiri


from sesheta.utils import calculate_pullrequest_size, set_size


daiquiri.setup(level=logging.DEBUG, outputs=('stdout', 'stderr'))
_LOGGER = daiquiri.getLogger(__name__)


def add_size_label(pullrequest: dict) -> None:
    """Add a size label to a GitHub Pull Request."""
    if pullrequest['title'].startswith('Automatic update of dependency'):
        return

    sizeLabel = calculate_pullrequest_size(pullrequest)

    _LOGGER.debug(
        f"Calculated the size of {pullrequest['html_url']} to be: {sizeLabel}")

    if sizeLabel:
        set_size(pullrequest['url'], sizeLabel)
