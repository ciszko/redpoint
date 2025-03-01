import pytest
from click.testing import CliRunner
from redpoint import cli
from redpoint.mappings import SPORT_MAPPING, BOULDER_MAPPING, OTHER_MAPPING, VALID_NAMES


@pytest.fixture(scope="module")
def runner():
    yield CliRunner()


def test_help(runner):
    result = runner.invoke(cli.main, ["--help"])
    assert result.exit_code == 0, "Wrong exit code"
    output = ("Usage", "Options", "Commands")
    assert all(x in result.output for x in output)


param_convert_all = (
    ("French", "6a", SPORT_MAPPING.keys()),
    ("V-Scale", "V5", BOULDER_MAPPING.keys()),
    ("Aid", "C2", OTHER_MAPPING.keys()),
)


@pytest.mark.parametrize(("system", "grade", "systems"), param_convert_all)
def test_convert_all(runner, system, grade, systems):
    result = runner.invoke(cli.main, ["convert", grade, system, "all"])
    assert result.exit_code == 0, "Wrong exit code"
    other_systems = [x for x in systems if system != x]
    assert all(x in result.output for x in other_systems), (
        "Grade was not converted into all systems"
    )


def test_convert_all_range(runner):
    result = runner.invoke(cli.main, ["convert", "6b", "French", "all", "--range"])
    assert result.exit_code == 0, "Wrong exit code"
    other_systems = [x for x in SPORT_MAPPING.keys() if x != "French"]
    assert all(x in result.output for x in other_systems), (
        "Grade was not converted into all systems"
    )


def test_convert_range(runner):
    result = runner.invoke(
        cli.main, ["convert", "V11", "V-Scale", "Fontainebleau", "--range"]
    )
    assert result.exit_code == 0, "Wrong exit code"
    assert "['8A']" in result.output, "Grade was not converted properly"


def test_convert(runner):
    result = runner.invoke(cli.main, ["convert", "8A", "Fontainebleau", "V-Scale"])
    assert result.exit_code == 0, "Wrong exit code"
    assert "V11" in result.output, "Grade was not converted properly"


param_compare = (
    ("8a", "French", "5.12a", "YDS", "harder"),
    ("5a", "French", "5.12a", "YDS", "easier"),
    ("7a+", "French", "5.12a", "YDS", "equal"),
)


@pytest.mark.parametrize(
    ("grade1", "system1", "grade2", "system2", "comparison"), param_compare
)
def test_compare(runner, grade1, system1, grade2, system2, comparison):
    result = runner.invoke(cli.main, ["compare", grade1, system1, grade2, system2])
    assert result.exit_code == 0, "Wrong exit code"
    assert comparison in result.output, "Wrong comparison between the grades"


def test_system(runner):
    result = runner.invoke(cli.main, ["system", "Polish"])
    assert result.exit_code == 0, "Wrong exit code"
    all_grades = SPORT_MAPPING["Polish"].keys()
    assert all(grade in result.output for grade in all_grades), (
        "Not all grades were listed"
    )


def test_systems_all(runner):
    result = runner.invoke(cli.main, ["systems"])
    assert result.exit_code == 0, "Wrong exit code"
    all_systems = [x[0] for x in VALID_NAMES]
    assert all(system in result.output for system in all_systems), (
        "Not all systems were listed"
    )


param_systems = (
    ("--sport", SPORT_MAPPING.keys()),
    ("--boulder", BOULDER_MAPPING.keys()),
    ("--other", OTHER_MAPPING.keys()),
)


@pytest.mark.parametrize(("param", "systems"), param_systems)
def test_systems(runner, param, systems):
    result = runner.invoke(cli.main, ["systems", param])
    assert result.exit_code == 0, "Wrong exit code"
    assert all(system in result.output for system in systems), (
        "Not all systems were listed"
    )
