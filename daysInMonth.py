year = int(input("Enter the Year:   "))
month = int(input("Enter the Month:   "))

def isLeap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def days_in_month(year,month):
    if month>12 or month<1:
        return "invalid! Please enter valid month."
    monthsInYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeap(year) and month==2:
        return 29
    return monthsInYear[month-1]

days = days_in_month(year,month)
print(days)
        
        
    
    