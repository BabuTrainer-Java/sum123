num=int(input("Enter  number"))
s=0
n2=num
while num!=0:
    n1=num % 10
    s=s+(n1*n1*n1)
    num=num //10
if n2==s:
    print("the given number is  armstrong")
else:
    print("the  given  number is  not armstrong ")