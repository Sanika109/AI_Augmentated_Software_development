"""Utilities for calculating and reporting student CGPA."""

MAX_GRADE_POINTS = 10.0
MIN_GRADE_POINTS = 0.0
OUTSTANDING_THRESHOLD = 9.0
EXCELLENT_THRESHOLD = 8.0
GOOD_THRESHOLD = 7.0
SATISFACTORY_THRESHOLD = 6.0


def _validate_courses(courses: list[tuple[float, float]]) -> None:
    """Raise ValueError when courses are empty or contain invalid values."""
    if not courses:
        raise ValueError("courses must not be empty")

    for credits, grade_points in courses:
        if credits <= 0:
            raise ValueError("course credits must be greater than zero")
        if not MIN_GRADE_POINTS <= grade_points <= MAX_GRADE_POINTS:
            raise ValueError("grade points must be between 0 and 10")


def calculate_cgpa(courses: list[tuple[float, float]]) -> float:
    """Return the credit-weighted CGPA rounded to two decimal places."""
    _validate_courses(courses)
    total_credits = sum(credits for credits, _ in courses)
    weighted_grade_points = sum(
        credits * grade_points for credits, grade_points in courses
    )
    return round(weighted_grade_points / total_credits, 2)


def get_cgpa_category(cgpa: float) -> str:
    """Return the performance category for a CGPA on a 10-point scale."""
    if not MIN_GRADE_POINTS <= cgpa <= MAX_GRADE_POINTS:
        raise ValueError("CGPA must be between 0 and 10")

    if cgpa >= OUTSTANDING_THRESHOLD:
        return "Outstanding"
    if cgpa >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if cgpa >= GOOD_THRESHOLD:
        return "Good"
    if cgpa >= SATISFACTORY_THRESHOLD:
        return "Satisfactory"
    return "Needs Improvement"


def get_student_report(courses: list[tuple[float, float]]) -> dict[str, float | str]:
    """Return the calculated CGPA and its performance category."""
    cgpa = calculate_cgpa(courses)
    category = get_cgpa_category(cgpa)
    return {"cgpa": cgpa, "category": category}
