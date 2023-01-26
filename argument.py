def fi(x,y = "day"):
    y="evening"
    print(x,y)
fi("good","morning")

def f(x,y = "day"):
    print(x,y)
f("Good")

def c(x,y="good"):
    print(x,y)
c("hello","world")

def a(n):
    x=5
    print(x)
x=2
print(x)
a(x)
print(x)

def b(m):
    global x
    x=5
    print(x)
x=2
print(x)
b(c)
print(x)