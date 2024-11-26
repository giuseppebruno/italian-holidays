from datetime import datetime, timedelta

class italian_holidays():

	holiday_names = {
		(1, 1): "New Year's Day",
		(1, 6): "Epiphany",
		(4, 25): "Liberation Day",
		(5, 1): "Labor Day / May Day",
		(6, 2): "Republic Day",
		(8, 15): "Ferragosto",
		(11, 1): "All Saints' Day",
		(12, 8): "Feast of the Immaculate Conception",
		(12, 25): "Christmas Day",
		(12, 26): "St. Stephen's Day"
	}

	def __init__(self, custom_holidays = []):
		self._custom_holidays = custom_holidays

	def is_holiday(self, date):

		if not isinstance(date, (str, datetime)):
			raise ValueError("is_holiday accepts only string or datetime object")
		
		date_obj = date
		
		if isinstance(date, str):
			try:
				date_obj = datetime.strptime(date, '%Y-%m-%d')
			except ValueError:
				raise ValueError("Date must be in the format 'Y-m-d'")

		if (date_obj.month, date_obj.day) in self.holiday_names:
			return True

		if (date_obj.month, date_obj.day) == (self._easter(date_obj).month, self._easter(date_obj).day):
			return True
		
		if (date_obj.month, date_obj.day) == (self._easter_monday(date_obj).month, self._easter_monday(date_obj).day):
			return True

		for custom_holiday in self._custom_holidays:

			if not isinstance(custom_holiday, (str, datetime)):
				raise ValueError("Custom holidays must be a list of string or datetime objects")
			
			custom_date_obj = datetime.strptime(custom_holiday, '%m-%d') if isinstance(custom_holiday, str) else custom_holiday

			if (date_obj.month, date_obj.day) == (custom_date_obj.month, custom_date_obj.day):
				return True
			
			return False

	def holiday_name(self, date):

		if not isinstance(date, (str, datetime)):
			raise ValueError("holiday_name accepts only string or datetime object")
		
		date_obj = date

		if isinstance(date, str):
			try:
				date_obj = datetime.strptime(date, '%Y-%m-%d')
			except ValueError:
				raise ValueError("Date must be in the format 'Y-m-d'")
		
		if (date_obj.month, date_obj.day) in self.holiday_names:
			return self.holiday_names[(date_obj.month, date_obj.day)]

		if (date_obj.month, date_obj.day) == (self._easter(date_obj).month, self._easter(date_obj).day):
			return "Easter Sunday"
		
		if (date_obj.month, date_obj.day) == (self._easter_monday(date_obj).month, self._easter_monday(date_obj).day):
			return "Easter Monday"
		
		for custom_holiday in self._custom_holidays:

			if not isinstance(custom_holiday, (str, datetime)):
				raise ValueError("Custom holidays must be a list of string or datetime objects")
			
			custom_date_obj = datetime.strptime(custom_holiday, '%m-%d') if isinstance(custom_holiday, str) else custom_holiday
			
			if (date_obj.month, date_obj.day) == (custom_date_obj.month, custom_date_obj.day):
				return "Custom holiday"
				
		return None

	def _easter(self, date):
		'''
		***********************
		WORKS FROM 1900 TO 2199
		***********************
		'''
		gold_numbers = {
			0: 19, 1: 45, 2: 34, 3: 23, 4: 42, 5: 31, 6: 49, 7: 39, 8: 28,
			9: 47, 10: 36, 11: 25, 12: 44, 13: 33, 14: 22, 15: 41, 16: 30, 
			17: 48, 18: 38, 19: 27
		}
		cycle_19_year = 1918
		year = int(date.strftime('%Y'))
		modulo = (year + 1) % 19
		gold_number = gold_numbers[modulo]

		if gold_number <= 31:
			full_moon = datetime(year, 3, gold_number)
		else:
			full_moon = datetime(year, 4, gold_number - 31)

		if full_moon.weekday() == 6:
			easter_date = full_moon + timedelta(days=7)
		else:
			easter_date = full_moon + timedelta(days=(6 - full_moon.weekday()))

		if (easter_date.year - cycle_19_year) % 19 == 0:
			easter_date += timedelta(days=7)

		return easter_date

	def _easter_monday(self, date):
		return self._easter(date) + timedelta(1)