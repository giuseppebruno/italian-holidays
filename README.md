# ItalianHolidays

A simple Python helper class to determine Italian holidays with the possibility to set custom holidays. Easter holidays' calculation will work for dates between 1900-2199.

[![PyPI status](https://img.shields.io/pypi/status/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/italian-holidays.svg)](https://pypi.python.org/pypi/italian-holidays/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/italian-holidays)](https://pypi.python.org/pypi/italian-holidays/)
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

custom_holidays = ["01-03", "01-05"] # date format: month-day | in this example: 3 January, 5 January

# But accepts also array of datetime object
custom_holidays = [datetime(2021, 1, 3), datetime(2021, 1, 5)]

holidays = italian_holidays(custom_holidays) # or simply italian_holidays() if you have no custom holidays to set

# Passing string
is_holiday = holidays.is_holiday("2024-01-03")
print(is_holiday) # True

# Passing datetime object
day = datetime(2031, 4, 14)
is_holiday = holidays.is_holiday(day)
print(is_holiday) # True

# Getting holiday's name (return None if date is not an italian holiday, return 'Custom holiday' if is one of the given dates)
holiday_name = holidays.holiday_name("2020-11-01")
print(holiday_name) # All Saints' Day
```

## Licence

Source code can be found on [github](https://github.com/giuseppebruno/italian-holidays), licenced under [MIT](http://opensource.org/licenses/mit-license.php).

Developed by [Giuseppe Bruno](https://gbrunodev.it)