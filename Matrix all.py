r=int(input("Enter no.of.rows:"))
s=int(input("Enter no.of.columns:"))
def matrix(r,s):
    m=[]
    for i in range(r):
        a=[]
        for j in range(s):
            b=int(input("enter a number:"))
            a.append(b)
        m.append(a)
    return m
#sum of row columns
M=matrix(r,s)
print(M)
sum_r=[]
sum_c=[]
for i in M:
    print(sum(i),end=" ")
print()
for j in range(s):
    a=0
    for i in range(r):
        a+=M[i][j]
    sum_c.append(a)
for i in (sum_c):
    print(i,end=" ")
# Adittion of Two matrix
m1=matrix(r,s)
print(m1)
m2=matrix(r,s)
print(m2)
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(s):
        result[i][j]=m1[i][j]+m2[i][j]
for i in result:
    print(i)
#subtraction of two matrix

result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(s):
        result[i][j]=m1[i][j]-m2[i][j]
for i in result:
    print(i)
#Multiplication of Two matrix
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(s):
        for k in range(3):
            result[i][j]=result[i][j]+m1[i][k]*m2[k][j]
for i in result:
    print(i)
# to print identity
for i in range(r):
    for j in range(s):
        if (i==j):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
#condition for identity
f=1
for i in range(r):
    for j in range(s):
        if (i==j and M[i][j]!=1):
            f=0
            break
        elif(i!=j and M[i][j]!=0):
            f=0
            break
if f==1:
    print(M,"is identity")
else:
    print(M,"is not identity")
#scalar matrix
n=int(input())
for i in range(3):
    for j in range(3):
        if (i==j):
            print(n,end=" ")
        else:
            print("0",end=" ")
    print()
#left diagnal
c=M[0][0]+M[1][1]+M[2][2]
print(c)
d=m1[0][0]+m1[1][1]+m1[2][2]
print(d)
e=m2[0][0]+m2[1][1]+m2[2][2]
print(e)
# Right Diagnal
g=M[0][2]+M[1][1]+M[2][0]
h=m1[0][2]+m1[1][1]+m1[2][0]
k=m2[0][2]+m2[1][1]+m2[2][0]
print(g)
print(h)
print(k)
#  to print null matrix

for i in range(r):
    for j in range(s):
        if (i==j):
            print("0",end=" ")
        else:
             print("0",end=" ")
    print()
# condition for null matrix
for i in range(r):
    for j in range(s):
        print(M[i][j],end=" ")
    print()
if(M[0][0]==M[0][1]==M[0][2]==M[1][0]==M[1][1]==M[1][2]==M[2][0]==M[2][1]==M[2][2]==0):
    print(M,"is a Null matrix")
else:
    print(M," is not a Null matrix")
#condition for upper triangular and lower triangular
m3=matrix(r,s)
if(m3[0][0]==m3[0][1]==m3[0][2]==m3[1][0]==m3[1][1]==m3[2][0]==0):
    print(m3,"is upper triangular")
elif(m3[0][2]==m3[1][1]==m3[1][2]==m3[2][0]==m3[2][1]==m3[2][2]==0):
    print(m3,"is  lower triangular")
else:
    print(m3,"is not upper and lower triangular")
    



