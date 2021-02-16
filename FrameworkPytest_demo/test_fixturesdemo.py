import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_annotation_check(self):
        print("Iam the test case")

    def test_annotation_check1(self):
        print("Iam the test case1")

    def test_annotation_check2(self):
        print("Iam the test case2")
