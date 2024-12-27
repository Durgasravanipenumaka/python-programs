import math
def perfectsquare(a):
    root=math.sqrt(a)
    if (root)**2 == a:
        print(" It is a perfect square")
    else:
        print("It is not a perfect square")    
a=int(input("Enter the number:"))
perfectsquare(a)
 