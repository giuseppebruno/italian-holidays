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