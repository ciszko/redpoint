[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

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

