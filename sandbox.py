from inflammation.models import daily_mean
import numpy as np
assert np.array_equal(np.array([2, 0]), daily_mean(np.array([[2, 0], [4, 0]])))
assert np.array_equal(np.array([0, 0]), daily_mean(np.array([[0, 0], [0, 0]])))
assert np.array_equal(np.array([3, 4]), daily_mean(np.array([[1, 2], [3, 4], [5, 6]])))
