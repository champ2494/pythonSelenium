import pytest


@pytest.mark.xfail
def test_thirdpgm():
    print("Running third pgm")


@pytest.mark.smoke
@pytest.mark.skip
def test_trial():
    print("Running Trial testcases")




