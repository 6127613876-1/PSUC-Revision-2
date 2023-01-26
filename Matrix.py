def creatematrix():
    l1=[]
    for i in range(1,r+1):
        l2=[]
        for j in range(1,c+1):
            x=int(input("enter"))
            l2.append(x)
        l1.append(l2)
    print(l1)
    return l1
r=int(input("enter row="))
c=int(input("enter col="))
M1=creatematrix()
M2=creatematrix()

if len(M1)==len(M2[0]):
    sum=[]
    for i in range(len(M1)):
        a=[]
        for j in range(len(M1[0])):
            s=M1[i][j]+M2[i][j]
            a.append(s)
        sum.append(a)
    print(sum)
else:
    print("Row of first matrix is not equal to colum of second matrix")

def transposematrix():
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            print(M1[j][i],end=' ')
        print()
transposematrix()