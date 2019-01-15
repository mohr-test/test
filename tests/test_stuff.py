import pytest

def test_something():
  assert 1 == 1  

def test_failure():
  assert 1 == 1 

def test_more():
  assert 1 == 1

def test_more_stuff():
  assert 1 == 1

def test_test():
  assert 0 == 0

if __name__ == '__main__':
  pytest.main()
