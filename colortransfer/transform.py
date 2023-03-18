"""Implement transform.

Implement transform.

Usage:
    from colortransfer import transform

"""

# fmt: off
from typing import Callable

from numpy.typing import NDArray

# fmt: on


def transform(
    source: NDArray,
    target: NDArray,
    std: Callable[[NDArray], float],
    mean: Callable[[NDArray], float],
    subtract: Callable[[NDArray, NDArray], NDArray],
    multiply: Callable[[NDArray, float], NDArray],
) -> NDArray:
    """Transform arrays.

    Transform arrays using Reinhard method.

    Arguments:
        source: Source lab channel.
        target: Target lab channel.

    Returns:
        Transformed channel array.

    """
    std_source = std(source)
    std_target = std(target)
    mean_source = mean(source)
    difference = subtract(source, mean_source)
    ratio = std_target.__truediv__(std_source)
    return multiply(ratio, difference)
