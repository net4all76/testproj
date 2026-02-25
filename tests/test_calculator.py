import pytest

from src.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_two_positives(self):
        assert add(1, 2) == 3

    def test_with_zero(self):
        assert add(5, 0) == 5

    def test_two_negatives(self):
        assert add(-1, -2) == -3

    def test_positive_and_negative(self):
        assert add(3, -1) == 2


class TestSubtract:
    def test_basic(self):
        assert subtract(5, 3) == 2

    def test_result_negative(self):
        assert subtract(3, 5) == -2

    def test_with_zero(self):
        assert subtract(7, 0) == 7


class TestMultiply:
    def test_two_positives(self):
        assert multiply(3, 4) == 12

    def test_with_zero(self):
        assert multiply(5, 0) == 0

    def test_two_negatives(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="0으로 나눌 수 없습니다."):
            divide(5, 0)
