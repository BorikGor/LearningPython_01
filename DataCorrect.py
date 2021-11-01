day = input("Please enter the day of the month:")
if day.isnumeric():
    if (int(day) < 32) & (int(day) > 0):
        pass
    else:
        print('Day entered incorrectly')
        exit() # todo: good idea to use exit()
else:
    print('Day entered incorrectly')
    exit()
# todo: too much rows of code. By condition month should be only number
mnth = input("Please enter the month:")
match mnth:
    case "01" | "1" | "Jan" | "jan" | "January" | "january":
        mnth = "January"
    case "02" | "2" | "Feb" | "February" | "february":
        mnth = "February"
        if int(day) > 29:
            print("Incorrect date.\nFebruary has at most 29 days.")
            exit()
    case "03" | "3" | "Mar" | "March" | "march":
        mnth = "March"
    case "04" | "4" | "Apr" | "April" | "april":
        mnth = "April O'neil"
        if int(day) > 30:
            print("Incorrect date.\nApril has only 30 days.")
            exit()
    case "05" | "5" | "May" | "may":
        mnth = "May"
    case "06" | "6" | "Jun" | "June" | "june":
        mnth = "June"
    case "07" | "7" | "Jul" | "July" | "july":
        if int(day) > 30:
            print("Incorrect date.\nJune has only 30 days.")
            exit()
        mnth = "July"
    case "08" | "8" | "Aug" | "August" | "august":
        mnth = "August"
    case "09" | "9" | "Sep" | "September" | "september":
        mnth = "September"
        if int(day) > 30:
            print("Incorrect date.\nSeptember has only 30 days.")
            exit()
    case "10" | "10" | "Oct" | "October" | "october":
        mnth = "October"
    case "11" | "11" | "Nov" | "November" | "november":
        mnth = "November"
        if int(day) > 30:
            print("Incorrect date.\nNovember has only 30 days.")
            exit()
    case "12" | "12" | "Dec" | "December" | "december":
        mnth = "December"
    case _:
        print("Month entered incorrectly.")
        exit()

for i in range(0, 4):
    yer = input("Please enter the year (this, or last century):")
    if int(yer) < 100:
        i += i
        if i > 4:
            print(yer, " is an incorrect year for this program.")
            exit()
        else:
            print("Please enter 4 digits for the year")

    else:
        break
match int(yer) % 4:
    case 0:
        match mnth:
            case "February":
                if int(day) > 29:
                    print("Incorrect date, February had only 29 days in the year", yer, ".")
                    exit()
            case _:
                print("Something's wrong with the day.")
                exit()
    case 1 | 2 | 3:
        match mnth:
            case "February":
                if int(day) > 28:
                    print("Incorrect date, February had only 28 days in the year", yer, ".")
                    exit()
            case _:
                print("Something's wrong with the day.")
                exit()

print("The date you've entered is: ", day, "/", mnth, "/", yer, ".")
