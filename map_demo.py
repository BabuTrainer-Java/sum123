from functools import reduce
l2=[]
numbers=[1,2,3,4,5]
print(" before  modifying::", numbers)
s=map(lambda x:x*2,numbers)
print(" after  modifying::", s)
t=(10,20,30,40)
for  x1 in t:
    l2.append(x1)
print(l2)
s2=map(lambda y:y*3,t)
l2=list(s2)
print("modification of tuple objs::",l2)
l5=[35,45,56,49,34,50,67,23,32]
s3=filter(lambda x:x > 35,l5)
l6=list(s3)
print("above  35 marks::",l6)
l7=[1,2,3,4,5]
s5=reduce(lambda x,y:x*y,l7)
print("reduce fun:::",s5)

points = [(1, 2), (4, 1), (5, -1), (2, 3)]
points.sort(key=lambda point: point[1])
print(points)  # Output: [(5, -1), (4, 1), (1, 2), (2, 3)]


