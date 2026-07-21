import pytest
from auth import authenticate

def test_authenticate_success():
    users = {'alice': {'name': 'Alice'}}
    assert authenticate(users, 'alice') == 'ALICE'

def test_authenticate_missing_user():
    users = {'alice': {'name': 'Alice'}}
    assert authenticate(users, 'bob') is None

def test_authenticate_missing_name_key():
    users = {'alice': {}}
    assert authenticate(users, 'alice') is None

def test_authenticate_empty_dict():
    assert authenticate({}, 'anything') is None