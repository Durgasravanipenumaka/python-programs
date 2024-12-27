# convert kilometer into miles and viceversa
a=float(input("enter the distance in kilometers:"))
b=float(input("enter the distance in miles:"))
miles=a*0.621371
kilometers=b*1.60934
print("conversion of ",a,"kilometers into ",miles,"miles")
print("conversion of",b,"miles into ",kilometers,"kilometers")


# converstion of Bytes into KB,MB,GB,and TB
a=float(input("Enter the number of bytes:"))
b=(1/1024)*a
print(a,"bytes in",b,"kilo bytes")
c=(1/(1024*1024))*a
print(a,"bytes in",c,"Mega bytes")
c=(1/(1024*1024*1024))*a
print(a,"bytes in",c,"Giga bytes")
c=(1/(1024*1024*1024*1024))*a
print(a,"bytes in",c,"Tera bytes")




