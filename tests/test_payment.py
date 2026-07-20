import pytest
from payment import calculate_discount

def test_calculate_discount_normal():
    assert calculate_discount(10, 20) == 0.5

def test_calculate_discount_zero_total():
    assert calculate_discount(10, 0) == 0.0