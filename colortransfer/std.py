"""Implement std.

This module implement std.

Usage:
    from colortransfer import std

"""

# fmt: off
from typing import Callable

from numpy.typing import NDArray

# fmt: on

std: Callable[[NDArray], float]
