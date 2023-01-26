def func(n):
    x=0
    y=1
    print(x)
    print(y)
    for i in range(0,n):
        z=x+y
        print(z)
        x=y
        y=z
n=int(input("Enter:"))
func(n)