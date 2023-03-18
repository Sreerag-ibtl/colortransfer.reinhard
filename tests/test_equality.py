"""Assert equality.

This module implements test function that assert equality of two objects.

Usage:
    python -m pytest -m -n auto tests.test_equality

"""

# fmt: off
from typing import Any, Callable
from unittest import TestCase

import pytest
from cv2 import imread
from numpy.typing import NDArray

from colortransfer import get_lab_split

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

im_path = "tests/test.jpg"

test_case = TestCase()
assert_equal = test_case.assertEqual

image = imread(im_path)
im_height, im_width = image.shape[:2]

lab = get_lab_split(image)

l_height, l_width = lab[0].shape
a_height, a_width = lab[1].shape
b_height, b_width = lab[2].shape


@pytest.mark.parametrize(
    "lhs, rhs, assert_equality",
    (
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
