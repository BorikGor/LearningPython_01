nmbr = input("Enter the number you'd like to check:")
match int(nmbr):
    case 0|1|2|3:
        print("It's a Prime Number.")
        exit()
    case _:
        for i in range(2, 1+int(nmbr)//2): #todo: good idea to check only half of whole range
            if (int(nmbr) % i):
                prime = True
                print("Checked", i, ", looks prime.")
            else:
                prime = False
                print("Checked", i, ", it's not prime.")
                break
if prime:
    print("It's a prime number!")
else:
    print("It's not a prime number.")