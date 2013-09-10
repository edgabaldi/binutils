#!/usr/bin/env python

import datetime

today = datetime.datetime.today()

week = today.isocalendar()[1]

year = today.year

print '%s%s' % (year, week)
