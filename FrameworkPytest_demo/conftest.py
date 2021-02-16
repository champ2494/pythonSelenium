import pytest


@pytest.fixture(scope="class")
def setup():
    print("Iam first")

    yield
    print("Iam Last")


@pytest.fixture()
def dataLoad():
    print("User profile created")
    return ["Rahul", "shetty"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
