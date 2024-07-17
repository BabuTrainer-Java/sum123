
my_list1=[1,2,3,4,2,2,4,5]

my_list1 = [9 if x == 2 or x==4 else x for x in my_list1]
print(my_list1)
my_list1 = ["even" if x%2==0 else "odd" for x in my_list1]
print(my_list1)

my_list=[1,2,3,4,2,2,4,5]
l=[]
for x in  my_list:
    if x % 2==0:
        l.append(x)
print("Even:::",l)