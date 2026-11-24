import random
import subprocess
import sys
from pathlib import Path

import pytest

from q_sort import quicksort


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ],
)
def test_quicksort_examples(numbers, expected):
    assert quicksort(numbers) == expected



# @pytest.mark.parametrize(
#     "input_text, expected",
#     [
#         ("5\n5\n4\n3\n2\n1\n", "1\n2\n3\n4\n5\n"),
#     ],
# )
# def test_command_line(input_text, expected):
#     result = subprocess.run(
#         [sys.executable, str(Path(__file__).with_name("q_sort.py"))],
#         input=input_text,
#         capture_output=True,
#         text=True,
#         check=True,
#         timeout=30,
#     )
#     assert result.stdout == expected
#     assert result.stderr == ""