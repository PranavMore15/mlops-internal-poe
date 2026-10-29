# test_hello.py
# Pytest Test Case / basic test script to satisfy the pytest requirement
from hello import add, greet

def test_add():
    assert add(2, 3) == 5

def test_greet():
    assert greet("DevOps") == "Hello, DevOps! Welcome to MLOps UAT Environment."