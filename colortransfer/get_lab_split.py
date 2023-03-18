"""Implement get_lab_split.

This module contain the implementation of get_lab_split.

Usage:
    from colortransfer import get_lab_split

"""

# fmt: off
from typing import Callable, Tuple

from numpy.typing import NDArray

# fmt: on

get_lab_split: Callable[[NDArray], Tuple[NDArray]]
