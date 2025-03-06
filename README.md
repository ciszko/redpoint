[![Python Versions](https://img.shields.io/badge/Python%20Version-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?style=flat)](https://pypi.org/project/redpoint/)

[![Coverage Status](https://coveralls.io/repos/github/ciszko/redpoint/badge.svg?branch=master&kill_cache=1)](https://pypi.org/project/redpoint/)

# 🔴 redpoint

Converting climbing grades made easy!

`🔴 redpoint` is a Python library that simplifies climbing grade conversions.  It supports a wide range of climbing grade systems (sport, bouldering, and more) from thecrag.com, allowing users to easily convert between systems (e.g., YDS to French), compare the difficulty of grades, and even generate ranges of equivalent grades.

## Overview

Converting the grades between the systems:

```python
from redpoint import Grade

Grade("5.12a", "YDS").to("French")  # <7a+, 'French'>
```

when typing `Grade` gets tedious, individual systems can be imported as well:

```python
from grading.systems import YDS

YDS("5.12a").to("French")  # <7a+, 'French'>
```

Comparing the difficulty of grades:

```python
Grade("5.14a", "YDS") > Grade("8a", "French")  # True
Grade("V11", "V-Scale") == Grade("8A", "Fontainebleau")  # True
UIAA("4") >= Ewbanks("33")  # False
```

Getting the range of the grade in different system:

```python
Brittish("5a").to_range("French")  # [<5b, 'French'>, <5b+, 'French'>, <5c, 'French'>, <5c+, 'French'>, <6a, 'French'>]
```

For the full list of features check out the [documentation](https://ciszko.github.io/redpoint/).

## Installation

redpoint is available on Pypi and can be installed with:

```shell
python -m pip install redpoint
```

## Supported systems

`🔴 redpoint` supports all the systems available on [thecrag.com](https://www.thecrag.com/en/article/gradesonthecrag):

Values after a comma represent corresponding class names from `redpoint.systems`, thus can be used to initialize the class.

**Sport**:
- Band Sport (difficulty levels), `BandSport`
- Ewbanks, `Ewbanks`
- YDS, `YDS`
- NCCS Scale, `NCCS`
- French, `French`
- British Tech., `British`
- UIAA, `UIAA`
- South African, `SouthAfrican`
- Old South African, `OldSouthAfrican`
- Saxon, `Saxon`
- Finnish, `Finnish`
- Norwegian, `Norwegian`
- Polish, `Polish`
- Brazil Technical, `Brazilian`
- Swedish, `Swedish`
- Russian, `Russian`

**Boulder**:
- Band Boulder (difficulty levels), `BandBoulder`
- V-Scale, `VScale`
- B-Scale, `BScale`
- S-Scale, `SScale`
- P-Scale, `PScale`
- Joshua Tree Scale, `JoshuaTree`
- Fontainebleau, `Font`
- Annot B-Scale, `AnnotBScale`
- Font Traverse, `FontTraverse`

**Other systems**:
- Band Other (difficulty levels), `BandOther`
- Aid, `Aid`
- Alpine Ice, `AlpineIce`
- Water Ice, `WaterIce`
- Mixed Rock/Ice, `RockIce`
- Ferrata Schall, `FerrataSchall`
- Ferrata Num, `FerrataNum`
- Ferrata French, `FerrataFrench`
- Scottish Winter Technical, `ScottishWinter`

## CLI

`🔴 redpoint` comes with a built-in CLI, so that you can convert the grades straight from the terminal. After installing the package
run:
```sh
redpoint --help
```
to see the available commands:
```sh
Usage: redpoint [OPTIONS] COMMAND [ARGS]...

  Redpoint: Climbing grade conversion tool.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  compare  Compares the difficulty between two grades.
  convert  Converts the grade into desired system.
  system   Lists all grades from desired system.
  systems  Lists supported climbing grade systems.
```
