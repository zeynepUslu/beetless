import pytest

from beetless import backend


def test_get_artists_empty():
    assert backend.get_artists() == []


def test_get_albums_empty():
    assert backend.get_albums() == []


@pytest.mark.skipif('True')
def test_get_tracks_empty():
    assert backend.get_tracks() == []
