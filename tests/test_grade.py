import pytest

from redpoint import Grade, UnknownSystem, UnknownGrade, ConversionError


value_system_param = (
    ("Beginner", "Band Sport"),
    ("12", "Ewbanks"),
    ("5.5", "YDS"),
    ("F5", "NCCS Scale"),
    ("3c+", "French"),
    ("4a", "British Tech."),
    ("4", "UIAA"),
    ("12", "South African"),
    ("F1", "Old South African"),
    ("III", "Saxon"),
    ("4", "Finnish"),
    ("4", "Norwegian"),
    ("IV", "Polish"),
    ("III", "Brazil Technical"),
    ("4-", "Swedish"),
    ("3B", "Russian"),
)


@pytest.mark.parametrize(("value", "system"), value_system_param)
def test_creating_grade(value, system):
    assert Grade(value, system)


def test_non_existing_system():
    with pytest.raises(UnknownSystem):
        Grade("6a", "Non existing system")


def test_non_existing_grade():
    with pytest.raises(UnknownGrade):
        Grade("12a", "French")


def test_conversion_error_different_types():
    with pytest.raises(ConversionError):
        Grade("6a", "French").to("V-Scale")


def test_adding_outside_of_range():
    with pytest.raises(UnknownGrade):
        Grade("9c", "French") + 10


def test_substracting_outside_of_range():
    with pytest.raises(UnknownGrade):
        Grade("1a", "French") - 10


@pytest.mark.parametrize(("value1", "system1"), value_system_param)
@pytest.mark.parametrize(("value2", "system2"), value_system_param)
def test_equality(value1, system1, value2, system2):
    assert Grade(value1, system1) == Grade(value2, system2), "Grades are not equal"


def test_equality_non_grade():
    assert Grade("VI.6", "Polish") != 2


def test_less_or_equal():
    assert Grade("5a", "French") <= Grade("VI.1", "Polish")


def test_less_than_non_grade():
    with pytest.raises(TypeError):
        Grade("8a", "French") < 50


def test_greater_than_non_grade():
    with pytest.raises(TypeError):
        Grade("8a", "French") > 2


def test_greater_or_equal():
    assert Grade("7a", "French") >= Grade("VI.1", "Polish")


def test_next_grade():
    assert Grade("5.12a", "YDS").next().value == "5.12b", "Next grade is not correct"


def test_previous_grade():
    assert Grade("5.12a", "YDS").previous().value == "5.11d"


def test_to_range():
    _range = Grade("4c", "British Tech.").to_range("French")
    grades = (
        Grade("4c", "French"),
        Grade("4c+", "French"),
        Grade("5a", "French"),
        Grade("5a+", "French"),
        Grade("5b", "French"),
    )
    for grade in _range:
        assert grade in grades


def test_to_range_error():
    with pytest.raises(ConversionError):
        Grade("VI-", "Polish").to_range("V-Scale")


mapping_method_param = (("min", "5c"), ("avg", "5c+"), ("max", "6a"))


@pytest.mark.parametrize(("method", "result"), mapping_method_param)
def test_system_conversion(method, result):
    assert Grade("5.10a", "YDS").to("French", method).value == result
