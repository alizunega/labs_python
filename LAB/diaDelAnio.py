##def is_year_leap(year):
##    if year % 4 != 0: 
##        return False
##    elif year % 4 == 0 and year % 100 != 0: 
##        return True
##    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
##        return False
##    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
##        return True
##
##
##
##def days_in_month(year, month):
##    if year < 1582 or month < 1 or month > 12:
##        return None
##    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##    res  = days[month - 1]
##    if month == 2 and is_year_leap(year):
##        res = 29
##    return res    


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


##def days_in_month(year, month):
##    if year == 0 or month == 0 or month > 13:
##        return None
##    elif is_year_leap(year) and month == 2:
##        return 29
##    elif month == 2 and is_year_leap(year) == False:
##        return 28
##    elif month == 4 or month == 6 or month == 9 or month == 11:
##        return 30
##    else:
##        return 31

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
