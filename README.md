[![Python Versions](https://img.shields.io/badge/Python%20Version-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?style=flat)](https://pypi.org/project/redpoint/)

[![Coverage Status](https://coveralls.io/repos/github/ciszko/redpoint/badge.svg?branch=master)](https://pypi.org/project/redpoint/)

# 🔴 red-point

Converting climbing grades made easy!

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

For a full list of features check out the documentation

