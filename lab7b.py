#!/usr/bin/env python3
# Student ID: smucadaon
class Time:

	def __init__(self,hour=12,minute=0,second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

def format_time(t):

	return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):

	sum = Time(0,0,0)
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	while sum.second >= 60:
		sum.second -= 60
		sum.minute += 1
	while sum.minute >= 60:
		sum.minute -= 60
		sum.hour += 1
	return sum

def valid_time(t):
	if t.hour < 0 or t.minute < 0 or t.second < 0:
		return False
	if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
		return False
	return True

def change_time(time, seconds):
	time.second += seconds
	while time.second < 0:
		time.second += 60
		time.minute -=1
	while time.minute < 0:
		time.minute += 60
		time.hour -= 1
	while time.second >= 60:
		time.second -= 60
		time.minute += 1
	while time.minute >= 60:
		time.minute -= 60
		time.hour += 1
