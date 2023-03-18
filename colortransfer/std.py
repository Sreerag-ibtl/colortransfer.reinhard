"""Implement std.

This module implement std.

Usage:
    from colortransfer import std

"""

# fmt: off
from typing import Callable

import numpy as np
from numpy.typing import NDArray

# fmt: on

std: Callable[[NDArray], float]

std = np.std
