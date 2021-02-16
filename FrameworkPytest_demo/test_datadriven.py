import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample:

    def test_editprofile(self, dataLoad):
        print(dataLoad[0], dataLoad[1])


