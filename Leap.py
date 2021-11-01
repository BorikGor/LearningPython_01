yer = input("Enter the year you want to check:\n")
print("The Year ",yer,"was", end="")
if (int(yer) % 4):
    print("n\'t a leap year")
else:
    print(" a leap year.")
exit()