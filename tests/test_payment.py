import pytest
from payment import calculate_discount

def test_calculate_discount_zero_total():
    assert calculate_discount(100, 0) == 0.0

def test_calculate_discount_valid():
    assert calculate_discount(100, 200) == 0.5