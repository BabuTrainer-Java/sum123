n1=int(input("Enter  a  number"))
n3=n1
s=0
while n1!=0:
    n2=n1%10
    s=s+n2+n2+n2
    n1=n1//10
if s==n3:
    print(" the given number is perfect")
else:
    print(" the given number is  not  perefct")