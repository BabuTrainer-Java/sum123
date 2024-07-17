def  emp(**k):
    print("Ename:::",k["ename"])
    for i  in k.items():
        print(i)
emp(eid=101,ename="nani",esal=18000)
def  emp1(*k2):
    for x in  k2:
        print(x)
emp1(10,20,30,40)
