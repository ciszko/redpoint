import pytest

from redpoint import (
    Grade,
    UnknownSystem,
    UnknownGrade,
    ConversionError,
    CONVERSION_METHOD,
    systems,
)


sport_system_param = (
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

boulder_system_param = (
    ("Beginner", "Band Boulder"),
    ("V4", "V-Scale"),
    ("B2-", "B-Scale"),
    ("S3", "S-Scale"),
    ("P10", "P-Scale"),
    ("D", "Joshua Tree Scale"),
    ("8B+", "Fontainebleau"),
    ("B14", "Annot B-Scale"),
    ("7C", "Font Traverse"),
)

other_system_param = (
    ("Beginner", "Band Other"),
    ("C4", "Aid"),
    ("AI6+", "Alpine Ice"),
    ("WI5", "Water Ice"),
    ("M9", "Mixed Rock/Ice"),
    ("D", "Ferrata Schall"),
    ("5", "Ferrata Num"),
    ("TD", "Ferrata French"),
    ("7", "Scottish Winter Technical"),
)
all_grade_param = sport_system_param + boulder_system_param + other_system_param


@pytest.mark.parametrize(("value", "system"), all_grade_param)
def test_creating_grade(value, system):
    assert Grade(value, system)


climbing_systems = (
    systems.BandSport,
    systems.Ewbanks,
    systems.YDS,
    systems.NCCS,
    systems.French,
    systems.British,
    systems.UIAA,
    systems.SouthAfrican,
    systems.OldSouthAfrican,
    systems.Saxon,
    systems.Finnish,
    systems.Norwegian,
    systems.Polish,
    systems.Brazilian,
    systems.Swedish,
    systems.Russian,
    systems.BandBoulder,
    systems.VScale,
    systems.BScale,
    systems.SScale,
    systems.PScale,
    systems.JoshuaTree,
    systems.Font,
    systems.AnnotBScale,
    systems.FontTraverse,
    systems.BandOther,
    systems.Aid,
    systems.AlpineIce,
    systems.WaterIce,
    systems.RockIce,
    systems.FerrataSchall,
    systems.FerrataNum,
    systems.FerrataFrench,
    systems.ScottishWinter,
)

creating_helper_grade_param = zip(all_grade_param, climbing_systems)


@pytest.mark.parametrize(("value", "system"), creating_helper_grade_param)
def test_creating_helper_grade(value, system):
    assert Grade(value[0], value[1]).value == system(value[0]).value


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


def test_adding_unsupported_type():
    with pytest.raises(TypeError):
        Grade("9c", "French") + "hello"


def test_substracting_unsupported_type():
    with pytest.raises(TypeError):
        Grade("1a", "French") - "hello"


@pytest.mark.parametrize(("value1", "system1"), sport_system_param)
@pytest.mark.parametrize(("value2", "system2"), sport_system_param)
def test_equality(value1, system1, value2, system2):
    assert Grade(value1, system1) == Grade(value2, system2), "Grades are not equal"


def test_equality_non_grade():
    assert Grade("VI.6", "Polish") != 2


def test_equality_different_systems():
    with pytest.raises(ConversionError):
        Grade("7a", "French") == Grade("V11", "V-Scale")


def test_less_or_equal():
    assert Grade("5a", "French") <= Grade("VI.1", "Polish")


def test_less_than_non_grade():
    with pytest.raises(TypeError):
        Grade("8a", "French") < 50


def test_less_than_different_systems():
    with pytest.raises(ConversionError):
        Grade("7a", "French") < Grade("V11", "V-Scale")


def test_greater_than_non_grade():
    with pytest.raises(TypeError):
        Grade("8a", "French") > 2


def test_greater_than_different_systems():
    with pytest.raises(ConversionError):
        Grade("7a", "French") > Grade("V11", "V-Scale")


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


mapping_method_param = (
    (CONVERSION_METHOD.MIN, "5c"),
    (CONVERSION_METHOD.AVERAGE, "5c+"),
    (CONVERSION_METHOD.MAX, "6a"),
)


@pytest.mark.parametrize(("method", "result"), mapping_method_param)
def test_system_conversion(method, result):
    assert Grade("5.10a", "YDS").to("French", method).value == result
