#!/bin/python
from datetime import datetime, timedelta
import sys

class italian_holidays():

	def __init__(self, custom_holidays = []):
		self._custom_holidays = custom_holidays

	def is_holiday(self, date):

		if isinstance(date, str) == False and isinstance(date, datetime) == False:
			return sys.exit('is_holiday can accept only string or datetime object')
		date_obj = date
		if isinstance(date, str):
			date_obj = datetime.strptime(date, '%Y-%m-%d')
		if date_obj is None:
			return sys.exit('date must be in the format \'Y-m-d\'')
		if date_obj.month == 1 and date_obj.day == 1:
			return True
		if date_obj.month == 1 and date_obj.day == 6:
			return True
		if date_obj.month == self._easter(date_obj).month and date_obj.day == self._easter(date_obj).day:
			return True
		if date_obj.month == self._easter_monday(date_obj).month and date_obj.day == self._easter_monday(date_obj).day:
			return True
		if date_obj.month == 4 and date_obj.day == 25:
			return True
		if date_obj.month == 5 and date_obj.day == 1:
			return True
		if date_obj.month == 6 and date_obj.day == 2:
			return True
		if date_obj.month == 8 and date_obj.day == 15:
			return True
		if date_obj.month == 11 and date_obj.day == 1:
			return True
		if date_obj.month == 12 and date_obj.day == 8:
			return True
		if date_obj.month == 12 and date_obj.day == 25:
			return True
		if date_obj.month == 12 and date_obj.day == 26:
			return True
		if len(self._custom_holidays) > 0:
			for custom_holiday in self._custom_holidays:
				if isinstance(custom_holiday, str) == False and isinstance(custom_holiday, datetime) == False:
					return sys.exit('custom holidays can accept only array of string or datetime object')
				custom_date_obj = custom_holiday
				if isinstance(custom_holiday, str):
					custom_date_obj = datetime.strptime(custom_holiday, '%m-%d')
				if date_obj.month == custom_date_obj.month and date_obj.day == custom_date_obj.day:
					return True
		return False

	def holiday_name(self, date):
		if isinstance(date, str) == False and isinstance(date, datetime) == False:
			return sys.exit('holiday_name can accept only string or datetime object')
		date_obj = date
		if isinstance(date, str):
			date_obj = datetime.strptime(date, '%Y-%m-%d')
		if date_obj is None:
			return sys.exit('date must be in the format \'Y-m-d\'')
		name = None
		if date_obj.month == 1 and date_obj.day == 1:
			name = 'New Year\'s Day'
		if date_obj.month == 1 and date_obj.day == 6:
			name = 'Epiphany'
		if date_obj.month == self._easter(date_obj).month and date_obj.day == self._easter(date_obj).day:
			name = 'Easter Sunday'
		if date_obj.month == self._easter_monday(date_obj).month and date_obj.day == self._easter_monday(date_obj).day:
			name = 'Easter Monday'
		if date_obj.month == 4 and date_obj.day == 25:
			name = 'Liberation Day'
		if date_obj.month == 5 and date_obj.day == 1:
			name = 'Labor Day / May Day'
		if date_obj.month == 6 and date_obj.day == 2:
			name = 'Republic Day'
		if date_obj.month == 8 and date_obj.day == 15:
			name = 'Ferragosto'
		if date_obj.month == 11 and date_obj.day == 1:
			name = 'All Saints\' Day'
		if date_obj.month == 12 and date_obj.day == 8:
			name = 'Feast of the Immaculate Conception'
		if date_obj.month == 12 and date_obj.day == 25:
			name = 'Christmas Day'
		if date_obj.month == 12 and date_obj.day == 26:
			name = 'St. Stephen\'s Day'
		if len(self._custom_holidays) > 0:
			for custom_holiday in self._custom_holidays:
				if isinstance(custom_holiday, str) == False and isinstance(custom_holiday, datetime) == False:
					return sys.exit('custom holidays can accept only array of string or datetime object')
				custom_date_obj = custom_holiday
				if isinstance(custom_holiday, str):
					custom_date_obj = datetime.strptime(custom_holiday, '%m-%d')
				if date_obj.month == custom_date_obj.month and date_obj.day == custom_date_obj.day:
					return 'Custom holiday'
		return name

	def _easter(self, date):
		''' 
		***********************
		WORKS FROM 1900 TO 2199
		***********************
		'''
		gold_numbers = {0: 19, 1: 45, 2: 34, 3: 23, 4: 42, 5: 31, 6: 49, 7: 39, 8: 28, 9: 47, 10: 36, 11: 25, 12: 44, 13: 33, 14: 22, 15: 41, 16: 30, 17: 48, 18: 38, 19: 27}
		cycle_19_year = 1918
		year = int(date.strftime('%Y'))
		modulo = (year + 1) % 19
		gold_number = gold_numbers[modulo]
		if gold_number <= 31:
			full_moon = datetime(year, 3, gold_number)
			easter_date = None
			if full_moon.weekday() == 6:
				easter_date = full_moon + timedelta(days= 7)
			else:
				easter_date = full_moon
				while easter_date.weekday() != 6:
					easter_date = easter_date + timedelta(days= 1)
			if (easter_date.year - cycle_19_year) % 19 == 0:
				easter_date = easter_date + timedelta(days=7)
			return easter_date
		else:
			day = gold_number - 31
			full_moon = datetime(year, 4, day)
			easter_date = None
			if full_moon.weekday() == 6:
				easter_date = full_moon + timedelta(days= 7)
			else:
				easter_date = full_moon
				while easter_date.weekday() != 6:
					easter_date = easter_date + timedelta(days= 1)
			return easter_date

	def _easter_monday(self, date):
		return self._easter(date) + timedelta(1)