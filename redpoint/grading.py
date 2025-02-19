from __future__ import annotations
from typing import Generator, Optional, TypedDict
from .mappings import (
    BOULDER_MAPPING,
    SPORT_MAPPING,
    NAMING_MAP,
    BOULDER_SYSTEMS,
    VALID_NAMES,
)


class UniversalGrade(TypedDict):
    start: int
    height: int


class METHOD_MAPPING:
    MIN = "min"
    AVERAGE = "avg"
    MAX = "max"


class SYSTEM_TYPE:
    SPORT = "SPORT"
    BOULDER = "BOULDER"


class UnknownGrade(BaseException):
    pass


class UnknownSystem(BaseException):
    pass


class ConversionError(BaseException):
    pass


class GradingSystem:
    """A class representing a grading system.

    For supported systems take a look at `VALID_SYSTEMS` list.
    `GradingSystem` supports the following operations:
    - can be iterated over `for x in system:`
    - can be indexed to return a `Grade` `GradingSystem("YDS")["5.8"]`
    """

    def __init__(self, name):
        try:
            system_name = NAMING_MAP[name.lower()]
        except KeyError as e:
            msg = f"System not found. Valid scale names are: {VALID_NAMES}"
            raise UnknownSystem(msg) from e

        if system_name in BOULDER_SYSTEMS:
            system_type = SYSTEM_TYPE.BOULDER
            mapping = BOULDER_MAPPING[system_name]
        else:
            system_type = SYSTEM_TYPE.SPORT
            mapping = SPORT_MAPPING[system_name]

        self.name = system_name
        self.system_type = system_type
        self.mapping = mapping

    def __getitem__(self, key):
        try:
            return self.mapping[key]
        except KeyError as e:
            msg = "Grade not found"
            raise UnknownGrade(msg) from e

    def __iter__(self) -> Generator[Grade, None, None]:
        return (Grade(x, self.name) for x in self.mapping.keys())

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name}, {self.system_type}"

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__str__()}>"

    def get_grade_index(self, key) -> tuple[UniversalGrade, int]:
        try:
            return next(
                (self.mapping[grade], i)
                for i, grade in enumerate(self.mapping.keys())
                if key == grade
            )
        except StopIteration:
            raise UnknownGrade("Grade outside of known range")

    def add_to_indexed_grade(self, system_index: int, offset: int) -> Grade:
        """Finds a grade that is `offset` in offset to `system_index` grade.

        Example:
            6a is a 30th grade of French-sport system. Adding the offset of
            2 will result in the 6b grade as it is the 2nd grade after 6a.

        Args:
            scale_index (int): The index of the base grade.
            offset (int): The offset that will be used to shift the base grade.

        Raises:
            UnknownGrade: When the resulting grade is outside of the known range.

        Returns:
            Grade: The resulting shifted grade.
        """
        try:
            grade = next(
                name
                for i, name in enumerate(self.mapping.keys())
                if i == system_index + offset
            )
        except StopIteration:
            raise UnknownGrade("Grade outside of known range")
        return Grade(grade, self.name)

    def get_range(self, universal_grade: UniversalGrade) -> list[Grade]:
        """Returns a range of `Grade`s from the universal value.

        Args:
            universal_grade (UniversalGrade): The universal value of a given grade.

        Returns:
            list[Grade]: The list of grades within the range of given `universal_grade`.
        """
        stop = universal_grade["start"] + universal_grade["height"]
        return [
            Grade(name, self.name)
            for (name, value) in self.mapping.items()
            if universal_grade["start"] <= value["start"] < stop
        ]

    def find_grade(self, universal_value: int) -> Optional[Grade]:
        """Returns a grade that matches the given universal value.

        Args:
            universal_value (int): The value of the grade in the universal system.

        Returns:
            Optional[Grade]: The grade that matches the universal value.
        """
        for name, value in self.mapping.items():
            if value["start"] < universal_value <= value["start"] + value["height"]:
                return Grade(name, scale=self.name)
        else:
            return None


class Grade:
    """A class representing one single grade from a given grading system.

    `Grade` supports the following operations:
    - adding (+ int), getting x harder grade
    - substracting (- int), getting x easier grade
    - comparing between grades of any system (`==`, `>`, `>`, `>=`, `<=`)

    Each grade has its own `universal_grade` which is used for conversion
    between the systems as well as for comparisons between the grades.
    """

    def __init__(self, value, scale):
        self.value = value
        self.system = GradingSystem(scale)
        universal_grade, system_index = self.system.get_grade_index(value)
        self.universal_grade = universal_grade
        self._system_index = system_index

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.value}, '{self.system.name}'"

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__str__()}>"

    def __add__(self, other) -> Grade:
        if isinstance(other, int):
            return self.system.add_to_indexed_grade(self._system_index, other)

    def __sub__(self, other) -> Grade:
        if isinstance(other, int):
            return self.system.add_to_indexed_grade(self._system_index, -other)

    def next(self) -> Grade:
        """Returns one grade harder.

        Returns:
            Grade: The harder grade.
        """
        return self.__add__(1)

    def previous(self) -> Grade:
        """Returns one grade easier.

        Returns:
            Grade: The easier grade,
        """
        return self.__sub__(1)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Grade):
            return False
        if other.system.name == self.system.name:
            return self.value == other.value
        self_stop = self.universal_grade["start"] + self.universal_grade["height"]
        other_stop = other.universal_grade["start"] + other.universal_grade["height"]
        return max(
            self.universal_grade["start"], other.universal_grade["start"]
        ) <= min(self_stop, other_stop)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Grade):
            msg = f"'<' not supported between instances of 'Grade' and {type(other)}"
            raise TypeError(msg)
        return (
            self.universal_grade["start"] + self.universal_grade["height"]
            < other.universal_grade["start"]
        )

    def __gt__(self, other) -> bool:
        if not isinstance(other, Grade):
            msg = f"'>' not supported between instances of 'Grade' and {type(other)}"
            raise TypeError(msg)
        return (
            self.universal_grade["start"]
            >= other.universal_grade["start"] + other.universal_grade["height"]
        )

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def _to_universal(self, method: METHOD_MAPPING = METHOD_MAPPING.AVERAGE) -> int:
        if method == METHOD_MAPPING.MIN:
            return self.universal_grade["start"]
        if method == METHOD_MAPPING.AVERAGE:
            return self.universal_grade["start"] + (self.universal_grade["height"] // 2)
        if method == METHOD_MAPPING.MAX:
            return self.universal_grade["start"] + self.universal_grade["height"] - 1

    def to(
        self, system_name: str, method: METHOD_MAPPING = METHOD_MAPPING.AVERAGE
    ) -> Grade:
        """Converts the grade to a given scale.

        Args:
            system_name (str): The grading system onto which the `grade` will be converted
            method (METHOD_MAPPING, optional): The method of conversion. Defaults to `METHOD_MAPPING.AVERAGE`.

        Returns:
            Grade: The converted grade
        """
        system = GradingSystem(system_name)
        if self.system.system_type != system.system_type:
            msg = f"Cannot convert {self.system.system_type} grade to {system.system_type} grade"
            raise ConversionError(msg)
        value = self._to_universal(method)
        return system.find_grade(value)

    def to_range(self, system_name) -> list[Grade]:
        """Converts the grade to all possible grades in another system.

        This method makes sense when converting onto a system that has a greater
        number of grades. For example In YDS (Yosemitee Decimal System) the grades
        span much more than in French.
        5.8 in YDS includes 4c+, 5a, 5a+ in French system.

        Args:
            system_name (str): The grading system onto which the `grade` will be converted

        Raises:
            ConversionError: When the given system type is different. BOULDER cannot be converted into SPORT and viceversa

        Returns:
            list[Grade]: The converted list of grades
        """
        system = GradingSystem(system_name)
        if self.system.system_type != system.system_type:
            msg = f"Cannot convert {self.system.system_type} grade to {system.system_type} grade"
            raise ConversionError(msg)
        return system.get_range(self.universal_grade)
