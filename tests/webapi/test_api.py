import pytest

import beetless.api

import json
import multiprocessing
import time
import urllib.request


@pytest.fixture(scope="module")
def opener(request):
    HOST = 'localhost'
    PORT = 1313

    class BeetlessOpener:

        def __init__(self):
            time.sleep(1)
            self._opener = urllib.request.build_opener()

        def get(self, url):
            full_url = "http://%s:%d/api/v1/%s" % (HOST, PORT, url)
            response = self._opener.open(full_url)
            raw_data = response.read().decode('utf-8')
            return json.loads(raw_data)

    server = multiprocessing.Process(target=beetless.api.start,
                                     kwargs={'port': PORT})
    server.start()

    def finalize():
        server.terminate()

    request.addfinalizer(finalize)
    return BeetlessOpener()


def test_get_artists(opener):
    assert opener.get('artists') == {'artists': []}


def test_get_albums(opener):
    assert opener.get('albums') == {'albums': []}
