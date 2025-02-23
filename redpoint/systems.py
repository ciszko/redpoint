"""
:code:`systems` includes helper classes to reduce using :code:`Grade` class.
Instead of writing :code:`Grade("7a", "French")` you can just write :code:`French("7a")`.
"""

from .grading import Grade


class BandSport(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Band Sport")


class Ewbanks(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Ewbanks")


class YDS(Grade):
    def __init__(self, value: str):
        super().__init__(value, "YDS")


class NCCS(Grade):
    def __init__(self, value: str):
        super().__init__(value, "NCCS Scale")


class French(Grade):
    def __init__(self, value: str):
        super().__init__(value, "French")


class British(Grade):
    def __init__(self, value: str):
        super().__init__(value, "British Tech.")


class UIAA(Grade):
    def __init__(self, value: str):
        super().__init__(value, "UIAA")


class SouthAfrican(Grade):
    def __init__(self, value: str):
        super().__init__(value, "South African")


class OldSouthAfrican(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Old South African")


class Saxon(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Saxon")


class Finnish(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Finnish")


class Norwegian(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Norwegian")


class Polish(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Polish")


class Brazilian(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Brazil Technical")


class Swedish(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Swedish")


class Russian(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Russian")


class BandBoulder(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Band Boulder")


class VScale(Grade):
    def __init__(self, value: str):
        super().__init__(value, "V-Scale")


class BScale(Grade):
    def __init__(self, value: str):
        super().__init__(value, "B-Scale")


class SScale(Grade):
    def __init__(self, value: str):
        super().__init__(value, "S-Scale")


class PScale(Grade):
    def __init__(self, value: str):
        super().__init__(value, "P-Scale")


class JoshuaTree(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Joshua Tree Scale")


class Font(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Fontainebleau")


class AnnotBScale(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Annot B-Scale")


class FontTraverse(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Font Traverse")


class BandOther(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Band Other")


class Aid(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Aid")


class AlpineIce(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Alpine Ice")


class WaterIce(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Water Ice")


class RockIce(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Mixed Rock/Ice")


class FerrataSchall(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Ferrata Schall")


class FerrataNum(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Ferrata Num")


class FerrataFrench(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Ferrata French")


class ScottishWinter(Grade):
    def __init__(self, value: str):
        super().__init__(value, "Scottish Winter Technical")
