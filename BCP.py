av=5
x=int(input("ENTC:"))
i=0
while(i<x):
    if i>av:
        print(f"we don't have {x} candy")
        print("out of stocks")
        break
    print("candy")
    i=i+1