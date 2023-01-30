def pt1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end='\t')
        print()
pt1(5)
print()

def pt2(m):
    for i in range(1,m+1):
        for j in range(1,i+1):
            print(j,end='\t')
        print()
pt2(5)
print()

def pt3(o):
    for i in range(o,0,-1):
        for j in range(1,i+1):
            print(i,end='\t')
        print()
pt3(5)
print()

def pt4(p):
    for i in range(p,0,-1):
        for j in range(1,i+1):
            print(j,end='\t')
        print()
pt4(5)
print()

def pt5(q):
        for i in range(1,q+ 1):
            if(i%2==0):
                for j in range(1,i+ 1):
                    if j%2== 0:
                        print(1,end=' ')
                    else:
                        print(0,end=' ')
            else:
               for j in range(1,i+1):
                    if j%2==0:
                        print(0,sep=' ')
                    else:
                        print(1,sep=' ')
pt5(5)
print()

def pt6(p):
    for i in range(1,p+1):
        for j in range(p,i-1,-1):
            print(j,end='\t')
        print()
pt6(5)
print()

def pt7(q):
    for i in range(1,q+1):
        for j in range(q,i-1,-1):
            print('*',end='\t')
        print()
pt7(5)
print()

def pt8(r):
    for i in range(1,r+1):
        for j in range(1,i+1):
            print('*',end='\t')
        print()
pt8(5)
print()

def pt9(r):
    for i in range(1,r+1):
            print(' '*(r-i)+'*'*i,end='\n')
pt9(5)
print()

def pt10(s):
    for i in range(0,s+1):
        print(' ' * i+'*'*(s-i),end='\n')
pt10(5)
print()