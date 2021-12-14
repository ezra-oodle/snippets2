from snippets2 import snippets2
import pytest

@pytest.fixture
def teal_colour():
    return ("#0AD2A0")

def test_Colours(my_colour):
    assert snippets2.Colours().oodle_teal == teal_colour