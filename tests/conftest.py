import pytest


class Conftest:

    def pytest_addoption(self, parser):
        parser.addoption("--source_file", action="store", help_text='Enter source file path')
        parser.addoption("--destination_file", action="store", help_text='Enter destination file path')

    @pytest.fixture
    def source_destination(self, request):
        params = {'source': request.config.getoption("--source_file"),
                  'destination': request.config.getoption("--destination_file")}

        return params
