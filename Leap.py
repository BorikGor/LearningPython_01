yer = input("Enter the year you want to check:\n")
print("The Year ",yer,"was", end="")
# todo: year 2100 is not a leap one
if (int(yer) % 4):
    print("n\'t a leap year")
else:
    print(" a leap year.")
exit()