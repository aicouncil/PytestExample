#pip install pytest

import pytest
from main import add,subtract,divide

def test_addition():
    assert add(3,5) == 8
    assert add(-1,-3) == -4

def test_subtract():
    assert subtract(3,4) == -1
    assert subtract(-1,-3) == 2


def test_divide():
    assert divide(12,4) == 3
    assert divide(16,-4) == -4