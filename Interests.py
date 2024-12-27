p=int(input("Enter the principle value:"))
t=int(input("Enter the time peroid:"))
r=int(input("Enter the Rate:"))
n=int(input("Number of compounding year:"))
r=r/100
SI=(p*t*r)/100
print("Simple Interst:",SI) 
A=p*(1+(r/n))**(n*t)
CI=A-p
print("compound Interst:",CI)