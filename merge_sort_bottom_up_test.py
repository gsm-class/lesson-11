import random
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT = Path(__file__).with_name("merge_sort_bottom_up.py")


def run_sort(numbers):
    input_text = f"{len(numbers)}\n" + "".join(f"{number}\n" for number in numbers)
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        capture_output=True,
        text=True,
        check=True,
        timeout=30,
    )
    return result.stdout


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([5, 4, 3, 2, 1], "1\n2\n3\n4\n5\n"),
    ],
)
def test_sort_examples(numbers, expected):
    assert run_sort(numbers) == expected
