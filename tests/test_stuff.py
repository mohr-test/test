import pytest

def test_something():
  assert 1 == 1  

def test_failure():
  assert 1 == 1 

def test_more():
  assert 1 == 1

def test_even_more():
  assert 1 == 1

if __name__ == '__main__':
  pytest.main()
