import pytest
import irspy


def test_sum_as_string():
    assert irspy.sum_as_string(1, 1) == "2"
