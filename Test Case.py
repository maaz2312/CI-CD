#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0
    assert subtract(5, 10) == -5

if __name__ == "__main__":
    pytest.main()

