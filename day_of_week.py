import math, sys

week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

expected_output = [
    'Monday',
    'Monday',
    'Saturday',
    'Thursday',
    'Friday',
    'Tuesday',
    'Thursday',
    'Monday',
    'Friday',
    'Saturday',
    'Wednesday',
    'Monday'
]

dates = [
    [2017, 10, 30],
    [2016, 2, 29],
    [2015, 2, 28],
    [29, 4, 12],
    [570, 11, 30],
    [1066, 9, 25],
    [1776, 7, 4],
    [1933, 1, 30],
    [1953, 3, 6],
    [2100, 1, 9],
    [2202, 12, 15],
    [7032, 3, 26]
]

def day_name(d):
    y,m,q = d
    y_cal = y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400)
    m_cal = math.floor((13 * (m+1)) / 5)
    i = (q + m_cal + y_cal)%7
    return week[i]

def zellers(d):
    y,m,q = d
    if m == 1:
        y -= 1
        m = 13
    elif m == 2:
        y -= 1
        m = 14
    return day_name([y,m,q])

def is_correct(n, name):
    return expected_output[n] == name

i = 0
for d in dates:
    name = zellers(d)
    print(name, is_correct(i, name))
    i += 1