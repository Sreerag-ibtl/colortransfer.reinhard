"""Run transform.

Run transform.

Usage:
    python -m main

"""

# fmt: off
from argparse import ArgumentParser, Namespace

from cv2 import COLOR_LAB2BGR, cvtColor, imread, imwrite, merge
from numpy.typing import NDArray

from colortransfer import get_lab_split, transform

# fmt: on

argument_parser: ArgumentParser
arguments: Namespace
source: NDArray

argument_parser = ArgumentParser(description=__doc__)

argument_parser.add_argument(
    "--source", help="Path to source image.", required=True
)  # ####
argument_parser.add_argument(
    "--target", help="Path to target image.", required=True
)  # ####
argument_parser.add_argument(
    "--result", help="Path to result image.", required=True
)  # ####

arguments = argument_parser.parse_args()

source = imread(arguments.source)
target = imread(arguments.target)

l_source, a_source, b_source = get_lab_split(source)
l_target, a_target, b_target = get_lab_split(target)

l_result = transform(l_source, l_target)
a_result = transform(a_source, a_target)
b_result = transform(b_source, b_target)

lab_result = merge((l_result, a_result, b_result))

bgr_result = cvtColor(lab_result, COLOR_LAB2BGR)

imwrite(arguments.result, bgr_result)
