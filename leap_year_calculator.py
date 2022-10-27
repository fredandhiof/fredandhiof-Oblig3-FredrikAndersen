def is_leap_year(year):
    if (year % 4000 != 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    return False
