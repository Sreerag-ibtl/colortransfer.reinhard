"""Assert equality.

This module implements test function that assert equality of two objects.

Usage:
    python -m pytest -m -n auto tests.test_equality

"""

# fmt: off
from typing import Any, Callable

# fmt: on


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
