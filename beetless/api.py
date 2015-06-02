# Copyright (c) 2015 H. Turgut Uyar <uyar@itu.edu.tr>
#
# This file is part of Beetless.
#
# Kurander is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Beetless is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Beetless.  If not, see <http://www.gnu.org/licenses/>.

"""Module containing the ReST API for Beetless."""

from beetless import bottle


@bottle.route('/api/v1/artists')
def get_artists():
    """Get the artists in the collection.

    :return: All artists in the collection.
    :rtype: dict[str, list]
    """
    return {'artists': []}


@bottle.route('/api/v1/albums')
def get_albums():
    """Get the albums in the collection.

    :return: All albums in the collection.
    :rtype: dict[str, list]
    """
    return {'albums': []}


def start(host='localhost', port=8080):
    """Start the API service.

    :param str host: Server address to bind to.
    :param int port: Server port to bind to.
    """
    bottle.run(host=host, port=port)


if __name__ == '__main__':
    start()
