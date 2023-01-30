m=[]
def showmatrix(r,c):
    for i in range(r):
        l =[]
        for j in range(c):
            y = int(input())
            l.append(y)
        m.append(l)
    return m
r = int(input("Enter the number of rows:\t"))
c = int(input("Enter the number of column:\t"))
print(showmatrix(r,c))

a=[]
def showmatrix(r1,c1):
    for i in range(r1):
        b =[]
        for j in range(c1):
            x = int(input())
            b.append(x)
        a.append(b)
    return a
r1= int(input("Enter the number of rows:\t"))
c1= int(input("Enter the number of column:\t"))
print(showmatrix(r1,c1))

result=[]
def matmultiply(m,a):
    for i in range(len(m)):
        res_row = []
        for j in range(len(a[0])):
            res_row.append(0)
        result.append(res_row)
    if len(m[0]) == len(a):
        for i in range(len(m)):
            for j in range(len(a[0])):
                for k in range(len(result)):
                    result[i][j] += m[i][k] * a[k][j]
        return result
print(matmultiply(m,a))