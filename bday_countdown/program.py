import datetime

def greeting():
    print('')
    print('-------------------------------------')
    print('    CHECK DAYS TILL YOUR BIRTHDAY    ')
    print('-------------------------------------')
    print("\nPress Ctrl-C to exit")
    name = input("Your name :")
    year = input("\nYear you were born[YYYY] :")
    month = input("Month you were born[Jan,Feb,Mar,etc.] :")
    day = input("Day you were born [1-31] :")

    return name, fix_input(year, month, day)

def fix_input(year, month, day):
    month_index = {
        "jan":1, "feb":2, "mar":3, "apr":4, "may":5,
        "jun":6, "jul":7, "aug":8, "sep":9, "oct":10,
        "nov":11, "dec":12
    }
    print("fix_input")
    day = int(day)
    year = int(year)
    month = month[:3].lower()

    if day not in range(32):
        print("Day {} is invalid!".format(day))
        return None

    if month not in month_index.keys():
        print("Month {} is not valid!".format(month))
        return None

    if year > datetime.date.today().year or year < 1200:
        print("Year {} is not valid!".format(year))
        return None
    print("llooks good")
    return datetime.date(year, month_index[month], day)

def analyze_date(name, bdate):
    now = datetime.date.today()
    #temp date, same year as bdate to avoid calculating years as days
    temp = datetime.date(year=bdate.year, month = now.month, day = now.day)
    days = bdate.day - now.day
    months = bdate.month - now.month

    if temp == bdate:
        print("\n Happy Birthday {}, Have a wonderful day!!".format(name))
    elif temp < bdate:
        if temp.month == bdate.month:
            print("\n Good news {}, your birthday is JUST {} days away!".format(name, (bdate - temp).days))
        else:
            print("Your birthday is still {0} day[s] away, be patient :)".format((bdate - temp).days))
    else:
        if temp.month == bdate.month:
            print("\n Oops!, missed your birthday by JUST {} days!, hope you had fun!".format((temp - bdate).days))
        else:
            print("Your birthday was {} days ago!, ".format((temp - bdate).days))


if __name__ == "__main__":
    try:
        while True:
            name, bdate = greeting()
            print("got name : {}, bdate:{}".format(name, bdate))
            if bdate:
                analyze_date(name, bdate)
    except KeyboardInterrupt as e:
        print("\n Thanks for sharing, Goodbye!")

    print("\n Program Terminated\n")
