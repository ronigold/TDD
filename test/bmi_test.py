import bmi
import pytest

@pytest.mark.parametrize(
    'weight, height ,expected_output',
    [
        (80, 1.90, 22.16),
        (90, 2, 22.5),
        (50, 1.70, 17.3),
        (60, 1.8,  18.52),
        (58, 1.65, 21.30),
        (100, 1.70, 34.6),
        (120, 1.60, 46.87)
    ]
)

def test_bmi(weight, height, expected_output):
    assert bmi.bmi(weight,height)==expected_output

@pytest.mark.parametrize(
    'weight, height ,expected_output',
    [
        (80, 1.90, 'Normal (healthy weight)'),
        (90, 2, 'Normal (healthy weight)'),
        (50, 1.70, 'Underweight'),
        (60, 1.8, 'Normal (healthy weight)'),
        (120, 1.65, 'Obese Class III (Very severely obese)')
    ]
)

def test_bmi_categories(weight, height, expected_output):
    assert bmi.bmi_categories(weight,height)==expected_output