[![Python Versions](https://img.shields.io/badge/Python%20Version-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?style=flat)](https://pypi.org/project/redpoint/)

[![Coverage Status](https://coveralls.io/repos/github/ciszko/redpoint/badge.svg?branch=master)](https://pypi.org/project/redpoint/)

# 🔴 redpoint

Converting climbing grades made easy!

`🔴 redpoint` is a Python library that simplifies climbing grade conversions.  It supports a wide range of climbing grade systems (sport, bouldering, and more) from thecrag.com, allowing users to easily convert between systems (e.g., YDS to French), compare the difficulty of grades, and even generate ranges of equivalent grades.

## Overview

Converting the grades between the systems:

```python
Grade("5.12a", "YDS").to("French")
>>> <7a+, 'French'>
```

Comparing the difficulty of grades:

```python
Grade("5.14a", "YDS") > Grade("8a", "French")
>>> True
Grade("V11", "V-Scale") == Grade("8A", "Fontainebleau")
>>> True
```

Getting the range of the grade in different system:

```python
Grade("5a", "Brittish Tech.").to_range("French")
>>> [<5b, 'French'>, <5b+, 'French'>, <5c, 'French'>, <5c+, 'French'>, <6a, 'French'>]
```

For the full list of features check out the [documentation](https://ciszko.github.io/redpoint/).

## Installation

redpoint is available on Pypi and can be installed with:

```shell
python -m pip install redpoint
```

## Supported systems

`🔴 redpoint` supports all the systems available on [thecrag.com](https://www.thecrag.com/en/article/gradesonthecrag):

**Sport**:
- Band Sport (difficulty levels)
- Ewbanks
- YDS
- NCCS Scale
- French
- British Tech.
- UIAA
- South African
- Old South African
- Saxon
- Finnish
- Norwegian
- Polish
- Brazil Technical
- Swedish
- Russian

**Boulder**:
- Band Boulder (difficulty levels)
- V-Scale
- B-Scale
- S-Scale
- P-Scale
- Joshua Tree Scale
- Fontainebleau
- Annot B-Scale
- Font Traverse

**Other systems**:
- Band Other (difficulty levels)
- Aid
- Alpine Ice
- Water Ice
- Mixed Rock/Ice
- Ferrata Schall
- Ferrata Num
- Ferrata French
- Scottish Winter Technical
