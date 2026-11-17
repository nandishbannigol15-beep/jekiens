import pytest
from salary import calculate_salary


def test_gross_salary():
    assert calculate_salary(50000) == 65000


def test_hra_and_da():
    assert calculate_salary(10000) == 13000


def test_zero_salary():
    assert calculate_salary(0) == 0


def test_another_salary():
    assert calculate_salary(20000) == 26000