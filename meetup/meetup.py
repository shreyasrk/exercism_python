#!/usr/bin/python
from datetime import datetime, timedelta

weekMap = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day, which_week):
    dt = datetime(year, month, 1)
    if which_week == 'teenth':
        dt = datetime(year, month, 13)
    elif which_week == 'last':
        dt = datetime(year, month+1, 1) - timedelta(days=1)

    while dt.weekday() != weekMap[day]:
        if which_week == 'last':
            dt -= timedelta(days=1)
        else:
            dt += timedelta(days=1)

    if which_week not in ['teenth', 'last']:
        week = int(which_week[:1]) - 1
        dt += timedelta(days=week*7)
        if dt.month != month:
            raise MeetupDayException('Invalid Month')

    return dt.date()
