import pytest

from src.cgpa import calculate_cgpa, get_cgpa_category, get_student_report


def test_calculate_cgpa_single_course() -> None:
    assert calculate_cgpa([(4, 8)]) == 8.0


def test_calculate_cgpa_weighted_average() -> None:
    # (4*8 + 3*9 + 2*7) / 9 = 73 / 9 = 8.11
    assert calculate_cgpa([(4, 8), (3, 9), (2, 7)]) == 8.11


@pytest.mark.parametrize(
    "courses",
    [
        [],
        [(0, 8)],
        [(4, -1)],
        [(4, 11)],
    ],
)
def test_calculate_cgpa_invalid_inputs(courses) -> None:
    with pytest.raises(ValueError):
        calculate_cgpa(courses)


@pytest.mark.parametrize(
    "cgpa, expected",
    [
        (10.0, "Outstanding"),
        (9.0, "Outstanding"),
        (8.99, "Excellent"),
        (8.0, "Excellent"),
        (7.99, "Good"),
        (7.0, "Good"),
        (6.99, "Satisfactory"),
        (6.0, "Satisfactory"),
        (5.99, "Needs Improvement"),
        (0.0, "Needs Improvement"),
    ],
)
def test_get_cgpa_category(cgpa: float, expected: str) -> None:
    assert get_cgpa_category(cgpa) == expected


@pytest.mark.parametrize("cgpa", [-1, 10.5])
def test_get_cgpa_category_invalid_inputs(cgpa: float) -> None:
    with pytest.raises(ValueError):
        get_cgpa_category(cgpa)


def test_get_student_report() -> None:
    report = get_student_report([(4, 8), (3, 9), (2, 7)])
    assert report == {"cgpa": 8.11, "category": "Excellent"}
