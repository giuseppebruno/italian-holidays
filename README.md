# ItalianHolidays

A simple Python helper class to determine Italian holidays. Easter holidays' calculation will work for dates between 1900-2199.

[![PyPI status](https://img.shields.io/pypi/status/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![GitHub license](https://img.shields.io/github/license/giuseppebruno/italian-holidays.svg)](https://github.com/giuseppebruno/italian-holidays/blob/master/LICENSE)

## Install

### Using Pip

```bash
pip install italian-holidays
```

## Usage

```python
from italian_holidays import italian_holidays
from datetime import datetime

holidays = italian_holidays()

# Passing string
is_holiday = holidays.is_holiday("2024-06-02")
print(is_holiday) # True

# Passing datetime object
day = datetime(2031, 4, 14)
is_holiday = holidays.is_holiday(day)
print(is_holiday) # True
```

## Licence

Source code can be found on [github](https://github.com/giuseppebruno/italian-holidays), licenced under [MIT](http://opensource.org/licenses/mit-license.php).

Developed by [Giuseppe Bruno](https://gbrunodev.it)