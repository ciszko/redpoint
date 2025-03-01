import click

from .grading import Grade, GradingSystem, SYSTEM_TYPE
from .mappings import SPORT_MAPPING, BOULDER_MAPPING, OTHER_MAPPING

BOLD = "\u001b[1m"
RESET = "\u001b[0m"


@click.group()
@click.version_option()
def main():
    """Redpoint: Climbing grade conversion tool."""
    pass


@main.command()
@click.argument("grade")
@click.argument("from_system")
@click.argument("to_system")
@click.option(
    "--range",
    type=bool,
    is_flag=True,
    help="Whether to convert into a range of grades.",
)
def convert(grade, from_system, to_system, range):
    """Converts the grade into desired system.

    Converts a \u001b[1mGRADE\u001b[0m from \u001b[1mFROM_SYSTEM\u001b[0m to \u001b[1mTO_SYSTEM\u001b[0m.
    If \u001b[1mTO_SYSTEM\u001b[0m is "all" the conversion is made to all possible systems.

    """
    if to_system.lower() == "all":
        from_grade = Grade(grade, from_system)
        system_type = from_grade.system.system_type
        if system_type == SYSTEM_TYPE.SPORT:
            mapping = SPORT_MAPPING
        elif system_type == SYSTEM_TYPE.BOULDER:
            mapping = BOULDER_MAPPING
        elif system_type == SYSTEM_TYPE.OTHER:
            mapping = OTHER_MAPPING

        other_systems = [s for s in mapping.keys() if from_grade.system.name != s]
        output = ""

        for system in other_systems:
            if range:
                converted_grade = [v.value for v in from_grade.to_range(system)]
            else:
                converted_grade = from_grade.to(system).value
            output += f"{system} => {converted_grade}\n"

        click.echo(output)
        return

    if range:
        converted_grade = [
            v.value for v in Grade(grade, from_system).to_range(to_system)
        ]
    else:
        converted_grade = Grade(grade, from_system).to(to_system).value
    click.echo(converted_grade)


@main.command()
@click.argument("grade1")
@click.argument("system1")
@click.argument("grade2")
@click.argument("system2")
def compare(grade1, system1, grade2, system2):
    """Compares the difficulty between two grades.

    Returns difficulty level of \u001b[1mGRADE1\u001b[0m from \u001b[1mSYSTEM1\u001b[0m
    in comparison to \u001b[1mGRADE2\u001b[0m from \u001b[1mSYSTEM2\u001b[0m"""
    grade1_obj = Grade(grade1, system1)
    grade2_obj = Grade(grade2, system2)
    if grade1_obj > grade2_obj:
        click.echo(f"{grade1} is harder than {grade2}")
    elif grade1_obj < grade2_obj:
        click.echo(f"{grade1} is easier than {grade2}")
    else:
        click.echo(f"{grade1} and {grade2} are equal in difficulty")


@main.command()
@click.argument("system_name")
def system(system_name):
    """Lists all grades from desired system."""

    system = GradingSystem(system_name)
    click.echo(BOLD + system.name + ":" + RESET)
    for grade in system:
        click.echo(f"  - {grade.value}")


@main.command()
@click.option("--sport", is_flag=True, help="Lists sport climbing systems.")
@click.option("--boulder", is_flag=True, help="Lists bouldering systems.")
@click.option("--other", is_flag=True, help="Lists other systems.")
def systems(sport, boulder, other):
    """Lists supported climbing grade systems.

    By default lists all available systems.
    """
    all_systems = {
        "Sport": SPORT_MAPPING.keys(),
        "Boulder": BOULDER_MAPPING.keys(),
        "Other": OTHER_MAPPING.keys(),
    }

    if not any([sport, boulder, other]):
        # If no flags are provided, list all systems
        for category, systems_list in all_systems.items():
            click.echo(f"{BOLD}{category} Systems:{RESET}")
            for system in systems_list:
                click.echo(f"  - {system}")
    else:
        if sport:
            click.echo(f"{BOLD}Sport Systems:{RESET}")
            for system in all_systems["Sport"]:
                click.echo(f"  - {system}")
        if boulder:
            click.echo(f"{BOLD}Boulder Systems:{RESET}")
            for system in all_systems["Boulder"]:
                click.echo(f"  - {system}")
        if other:
            click.echo(f"{BOLD}Other Systems:{RESET}")
            for system in all_systems["Other"]:
                click.echo(f"  - {system}")


if __name__ == "__main__":
    main()  # pragma: no cover
