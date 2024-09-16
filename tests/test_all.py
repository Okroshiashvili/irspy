import pytest
import src.irspy as irspy


def test_sum_as_string():
    assert irspy.sum_as_string(1, 1) == "2"
