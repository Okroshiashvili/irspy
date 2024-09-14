import pytest
import src


def test_sum_as_string():
    assert src.sum_as_string(1, 1) == "2"
