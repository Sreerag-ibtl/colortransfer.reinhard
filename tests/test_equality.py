"""Assert equality.

This module implements test function that assert equality of two objects.

Usage:
    python -m pytest -m -n auto tests.test_equality

"""

# fmt: off
from typing import Any, Callable
from unittest import TestCase

import numpy as np
import pytest
from cv2 import imread
from numpy.typing import NDArray

from colortransfer import get_lab_split, mean, std, transform

# fmt: on


assert_equal: Callable[[Any, Any], None]
test_case: TestCase
l: NDArray
a: NDArray
b: NDArray
l_height: int
l_width: int
a_height: int
a_width: int
b_height: int
b_width: int
im_height: int
im_width: int
im_path: str
image: NDArray
test_array: NDArray
expected_mean: float
calculated_mean: float
expected_std: float
calculated_std: float
expected_channel: NDArray
calculated_channel: NDArray
target_image_path: str

im_path = "tests/test.jpg"
source_image_path = "tests/test.jpg"
target_image_path = "tests/scream.jpg"
expected_mean = 1.0
expected_std = 0.816496580927726
in_array = np.array([0, 1, 2])

calculated_mean = mean(in_array)
calculated_std = std(in_array)

test_case = TestCase()
assert_equal = test_case.assertEqual

image = imread(im_path)
target = imread(target_image_path)
im_height, im_width = image.shape[:2]

lab = get_lab_split(image)
lab_target = get_lab_split(target)

l_height, l_width = lab[0].shape
a_height, a_width = lab[1].shape
b_height, b_width = lab[2].shape

lab_target_height = lab_target[0].shape[0]
lab_target_width = lab_target[0].shape[1]

l_new = transform(lab[0], lab_target[0])
l_new_height, l_new_width = l_new.shape[:2]


@pytest.mark.parametrize(
    "lhs, rhs, assert_equality",
    (
        (l_new_height, l_height, assert_equal),
        (l_new_width, l_width, assert_equal),
        (calculated_std, expected_std, assert_equal),
        (calculated_mean, expected_mean, assert_equal),
        (
            (l_height, a_height, b_height),
            (im_height, im_height, im_height),
            assert_equal,
        ),
        (
            (l_width, a_width, b_width),
            (im_width, im_width, im_width),
            assert_equal,
        ),  # #####
    ),
)
def test_equality(
    lhs: Any, rhs: Any, assert_equality: Callable[[Any, Any], None]
) -> None:
    """Test equality.

    Test equality of lhs and rhs using assert_equality.

    Arguments:
        lhs: Left hand side.
        rhs: Right hand side.
        assert_equality: Function asserting equality.

    Raises:
        AssertionError

    Returns:
        None

    """
    assert_equality(lhs, rhs)
