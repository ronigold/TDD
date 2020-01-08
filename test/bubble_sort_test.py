import bubble_sort
import pytest

@pytest.mark.parametrize(
    'input ,expected_output',
    [
        ([1,6,3,2,9], [1,2,3,6,9]),
        ([8,6,1,2,0], [0,1,2,6,8]),
        ([1,0,2,7,5], [0,1,2,5,7])
    ]
)
def test_bmi(input, expected_output):
    assert all([a == b for a, b in zip(bubble_sort.bubblesort(input), expected_output)])