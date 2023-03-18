"""Implement transform.

Implement transform.

Usage:
    from colortransfer import transform

"""

# fmt: off
from functools import partial
from typing import Callable

from numpy import add, multiply, subtract
from numpy.typing import NDArray

from colortransfer.mean import mean
from colortransfer.std import std

# fmt: on


def _transform(
    source: NDArray,
    target: NDArray,
    std: Callable[[NDArray], float],
    mean: Callable[[NDArray], float],
    subtract: Callable[[NDArray, NDArray], NDArray],
    multiply: Callable[[NDArray, float], NDArray],
    add: Callable[[NDArray, float], NDArray],
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
    mean_target = mean(target)
    difference = subtract(target, mean_target)
    ratio = std_target.__truediv__(std_source)
    product = multiply(ratio, difference)
    return add(product, mean_source)


transform = partial(
    _transform,
    std=std,
    mean=mean,
    subtract=subtract,
    multiply=multiply,
    add=add,  # ####
)  # #####
