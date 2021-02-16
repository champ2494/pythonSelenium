import pytest


@pytest.mark.smoke
def test_firstpgm():
    print("Hi")


def test_secondpgm():
    msg = "Hello"
    assert msg == "Hi", "string not matched"


def test_crossBro(crossBrowser):
    print(crossBrowser)


