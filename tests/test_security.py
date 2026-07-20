import pytest
from security import execute

def test_execute_valid_command():
    assert execute("ping") == "pong"
    assert execute("status") == "ok"

def test_execute_invalid_command():
    with pytest.raises(ValueError):
        execute("import os; os.system('ls')")

def test_execute_malicious_input():
    with pytest.raises(ValueError):
        execute("__import__('os').system('echo pwned')")