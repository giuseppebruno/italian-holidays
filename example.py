from italian_holidays import italian_holidays
from datetime import datetime

holidays = italian_holidays()

# Passing string
is_holiday = holidays.is_holiday("2024-06-02")
print(is_holiday)

# Passing datetime object
day = datetime(2031, 4, 14)
is_holiday = holidays.is_holiday(day)
print(is_holiday)


# Getting holiday's name (return None if date is not an italian holiday)
holiday_name = holidays.holiday_name("2024-06-02")
print(holiday_name) # Republic Day