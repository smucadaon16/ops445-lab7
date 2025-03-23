#!/usr/bin/env python3
# Student ID: smucadaon
class Time:
	"""Simple object type for time of the day.
		data attributes: hour, minute, second
		function attributes: __init__, __str__, __repr__
			time_to_sec
	"""
	def __init__(self,hour=12,minute=0,second=0):
		"""constructor for time object"""
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		'''return a string representation for the object self'''
		return  f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

	def __repr__(self):
		'''Return a detailed string representation for interactive shells.'''
		return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

	def sum_times(self, t2):
		tot_seconds = self.time_to_sec() + t2.time_to_sec()
		return sec_to_time(tot_seconds)

	def time_to_sec(self):
		'''convert a time object to a single integer representing the
		number of seconds from mid-night'''
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

def sec_to_time(seconds):
	'''convert a given number of seconds to a time object in
		hour, minute, second format'''
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time
