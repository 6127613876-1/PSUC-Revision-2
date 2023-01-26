try:
    x=int(input("Enter:"))
    print(x)
    if x is str():
        raise ValueError("Value Error")
        raise TypeError("Type Error")
    raise ZeroDivisionError("ZDE")
    raise NameError("NE")
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
except ZeroDivisionError as zde:
    print(zde)
except NameError as ne:
    print(ne)
except:
    print("something went wrong")