f=open("File1.txt","r")
c=0
a=0
x=[]
for i in f:
    c=c+len(i)
    x=x+i.split(" ")
    a+=1
print("no.of.lines:",a)
print("no.of.words:",len(x))
print("no.of.character:",c)
f.close()
f=open("File1.txt","r")
fr=f.read()
b=0
h=0
t=0
for o in fr:
    if o.isalpha()==True:
        b+=1
    elif o.isnumeric()==True:
        h+=1
    else:
        t+=1
print("no.of.alphabets:",b)
print("no.of.numbers:",h)
print("no.of.special characters:",t)
f.close()
