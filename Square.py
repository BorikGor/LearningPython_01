sqSide = input("Please enter square side:")
# todo: it is better to declare int(sqSide) and use it as variable (no need to convert sqSide to int several times)
sqPerimeter = 4*int(sqSide)
sqDiagonal = int(sqSide)*(2**0.5)
print("Perimeter:",sqPerimeter,"\nDiagonal:",sqDiagonal)