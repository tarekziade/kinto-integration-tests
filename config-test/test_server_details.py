import configparser
import pytest
import requests


@pytest.fixture
def conf():
    config = configparser.ConfigParser()
    config.read('manifest.ini')
    return config


def test_version(conf, env):
    response = requests.get(conf.get(env, 'reader_server') + '/__version__')
    data = response.json()

    expected_fields = {'version', 'source', 'name', 'build', 'commit'}

    # First, make sure that data only contains fields we expect
    for key in data:
        assert key in expected_fields

    # Then make the we only have the expected fields in the data
    for field in expected_fields:
        assert field in data


def test_heartbeat(conf, env):
    response = requests.get(conf.get(env, 'reader_server') + '/__heartbeat__')
    data = response.json()

    expected_fields = {'permission', 'cache', 'storage'}

    # First, make sure that data only contains fields we expect
    for key in data:
        assert key in expected_fields

    # Then make the we only have the expected fields in the data
    for field in expected_fields:
        assert field in data


