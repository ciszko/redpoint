import pytest

from redpoint import GradingSystem, UnknownSystem, UnknownGrade, ConversionError


def test_unknown_system():
    with pytest.raises(UnknownSystem):
        GradingSystem("Unknown system")


@pytest.mark.parametrize("name", ("Ewbanks", "AU", "Australia", "New Zealand"))
def test_different_names_same_system(name):
    assert GradingSystem(name=name).name == "Ewbanks"


def test_indexing():
    assert GradingSystem("French")["5a"], "Cannot index the system"


def test_indexing_error():
    with pytest.raises(UnknownGrade):
        GradingSystem("French")["5.12a"]


def test_iterating():
    for grade in GradingSystem("V-Scale"):
        assert grade


def test_grade_not_found():
    assert GradingSystem("UIAA").find_grade(5000) is None
