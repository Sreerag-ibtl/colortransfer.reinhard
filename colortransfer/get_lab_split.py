"""Implement get_lab_split.

This module contain the implementation of get_lab_split.

Usage:
    from colortransfer import get_lab_split

"""

# fmt: off
from functools import partial
from typing import Callable, Tuple

from cv2 import COLOR_BGR2LAB, cvtColor, split
from numpy.typing import NDArray

# fmt: on

bgr_to_lab: Callable[[NDArray], NDArray]
get_lab_split: Callable[[NDArray], Tuple[NDArray, NDArray, NDArray]]

bgr_to_lab = partial(cvtColor, code=COLOR_BGR2LAB)


def _get_lab_split(
    image: NDArray,
    bgr_to_lab: Callable[[NDArray], NDArray],
    split: Callable[[NDArray], Tuple[NDArray, NDArray, NDArray]],
) -> Tuple[NDArray, NDArray, NDArray]:
    """Get image split into L, A, B arrays.

    Get image split into L, A, B arrays.

    Arguments:
        image: Input image array in BGR color space.
        bgr_to_lab: Converts BGR color space into LAB color space.
        split: Split image into channels.

    Returns:
        Returns tuple of three arrays.

    """
    lab: NDArray = bgr_to_lab(image)
    return split(lab)


get_lab_split = partial(_get_lab_split, bgr_to_lab=bgr_to_lab, split=split)
