print("Hello!\nPlease enter the first number:\n")
fst=input()
print(fst,"\nNow enter the desired operation \"+-*/\":\n")
op=input()
print(fst,op,"\nNow enter the Second number:\n")
scnd=input()
ERR=0
match op:
    case '+':
     rslt = (int(fst) + int(scnd))
    case '-':
     rslt = int(fst)-int(scnd)
    case '*':
     rslt = int(fst)*int(scnd)
    case '/':
     rslt = float(fst) / float(scnd)
    case _:
        ERR=1
        print("Something's wrong")
if ERR==1:
 exit()
else:
 print(fst, op, scnd, "=", rslt)
 print("\n\rBFN!")