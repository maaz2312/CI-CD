import pytest
from main import subtract  # Import function from main.py

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0
    assert subtract(5, 10) == -5
