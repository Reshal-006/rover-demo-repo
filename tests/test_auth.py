import pytest
from auth import authenticate

def test_authenticate_invalid_user():
    assert authenticate({'alice': {'name': 'Alice'}}, 'bob') is None

def test_authenticate_missing_name():
    assert authenticate({'alice': {'id': 1}}, 'alice') is None

def test_authenticate_success():
    assert authenticate({'alice': {'name': 'Alice'}}, 'alice') == 'ALICE'

def test_authenticate_empty_input():
    assert authenticate({}, 'alice') is None