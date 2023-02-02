import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean


def test_everything_works():
 npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean
    test_array = np.array([[0, 0],
                            [0, 0],
                            [0, 0]])
    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(np.array([0, 0]), daily_mean(test_array))
    
    
@pytest.mark.parametrize(
"test, expected",
    [
     ([[0, -1],[0, 0],[-1, 0]], [-1, -1]),
    ([[-1, -1],[-1, -1],[1, 1]], [-1, -1]),
    ([[1, 2],[3, -10000.1],[1, 0]],[1, -10000.1])
    ]
    )
def test_daily_min(test, expected):
    from inflammation.models import daily_min
    npt.assert_array_equal(np.array(expected), daily_min(test))
    
    
@pytest.mark.parametrize(
"test, expected",
    [
     ([[0, -1],[0, 0],[-1, 0]], [0,0]),
    ([[-1, -1],[-1, -1],[1, 1]], [1, 1]),
    ([[1, 2],[3, 10000.1],[1, 0]], [3, 10000.1])
    ]
    )
def test_daily_max(test, expected):
    from inflammation.models import daily_max
    npt.assert_array_equal(np.array(expected), daily_max(test))

    
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min
    from pytest import raises
    with raises(TypeError):
        daily_min([['Cannot', 'min'], ['string', 'arguments']])
        
def test_daily_max_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min
    from pytest import raises
    with raises(TypeError):
        daily_min([['Cannot', 'min'], ['string', 'arguments']])
        
@pytest.mark.parametrize(
"test, expected",
    [([[0, 0], [0, 0], [0, 0]], [0, 0]),
    ([[1, 2], [3, 4], [5, 6]], [3, 4]),]
    )
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))
    
    
