eid=int(input("Enter  Eid"))
ename=input("Enter  Ename")
esal=int(input("Enter  Esal"))
deptno=int(input("Enter  Deptno"))
comm=int(input("Enter  Comm"))
c=0
for i  in  range(1,5):
    if deptno==i:
        esal=esal*5/100
        c=c+1
        break
        #print("Eid:::",eid,":::Ename:::",ename,"::esal:::",esal,"::Deptno::",deptno,"::comm::",comm)
    else:
        eid=0
        ename=""
        esal=0
        comm=0
if c==1 :
    print("Eid:::",eid,":::Ename:::",ename,"::esal:::",esal,"::Deptno::",deptno,"::comm::",comm)
else:
    print("Eid:::",eid,":::Ename:::",ename,"::esal:::",esal,"::Deptno::",deptno,"::comm::",comm)
    