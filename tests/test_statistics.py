import pytest

from src.statistics import mean, maximum, minimum


class TestMean:
    def test_basic(self):
        assert mean([1, 2, 3]) == 2.0

    def test_single_element(self):
        assert mean([5]) == 5.0

    def test_floats(self):
        assert mean([1.0, 2.0, 3.0]) == pytest.approx(2.0)

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="빈 리스트"):
            mean([])


class TestMaximum:
    def test_basic(self):
        assert maximum([3, 1, 2]) == 3

    def test_negative_numbers(self):
        assert maximum([-1, -5, -2]) == -1

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="빈 리스트"):
            maximum([])


class TestMinimum:
    def test_basic(self):
        assert minimum([3, 1, 2]) == 1

    def test_negative_numbers(self):
        assert minimum([-1, -5, -2]) == -5

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="빈 리스트"):
            minimum([])
