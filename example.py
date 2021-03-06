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

# Getting holiday's name (return None if date is not an italian holiday)
holiday_name = holidays.holiday_name("2020-11-01")
print(holiday_name) # All Saints' Day