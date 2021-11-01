summ = input("How many dollars do you want to deposit:")
prcnt = input("\nWhat will be the percentage:")
yers = input("\nFor how many years can you spare that sum:")
rslt=summ

for i in range(1, int(yers)):
    rslt = float(rslt)*(1+float(prcnt)*0.01)
    #print(rslt)

print("After ",yers," years you'll get your ",summ,"dollars turned into ",round(float(rslt),2),".")