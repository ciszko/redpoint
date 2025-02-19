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

