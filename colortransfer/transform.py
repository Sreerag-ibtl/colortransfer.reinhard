"""Implement transform.

Implement transform.

Usage:
    from colortransfer import transform

"""

# fmt: off
from typing import Callable

from numpy.typing import NDArray

# fmt: on

transform: Callable[[NDArray, NDArray], NDArray]
