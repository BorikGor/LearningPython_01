mnth = input("Which month do you want to check:")
match mnth:
    case "01"|"1"|"Jan"|"jan"|"January"|"january":
        print("January", end="")
        ssn="Winter"
    case "02"|"2"|"Feb"|"February"|"february":
        print("February", end="")
        ssn="Winter"
    case "03"|"3"|"Mar"|"March"|"march":
        print("March", end="")
        ssn="Spring"
    case "04"|"4"|"Apr"|"April"|"april":
        print("April O'neil", end="")
        ssn="Spring"
    case "05"|"5"|"May"|"may":
        print("May", end="")
        ssn="Spring"
    case "06"|"6"|"Jun"|"June"|"june":
        print("June", end="")
        ssn="Summer"
    case "07"|"7"|"Jul"|"July"|"july":
        print("July", end="")
        ssn="Summer"
    case "08"|"8"|"Aug"|"August"|"august":
        print("August", end="")
        ssn="Summer"
    case "09"|"9"|"Sep"|"September"|"september":
        print("September", end="")
        ssn="Autumn"
    case "10"|"10"|"Oct"|"October"|"october":
        print("October", end="")
        ssn="Autumn"
    case "11"|"11"|"Nov"|"November"|"november":
        print("November", end="")
        ssn="Autumn"
    case "12"|"12"|"Dec"|"December"|"december":
        print("December", end="")
        ssn="Winter"
    case "quit":

        exit()
    case _:
        print("Something's wrong.")
print(" is a",ssn,"month.")