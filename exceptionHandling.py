a=5
b=2
try:
    print("resource open")
    print(a/b)
    k=int(input("enter a value"))
    print(k)



except ZeroDivisionError as e:
    print("can't divide by zero")
except ValueError as e:
    print("invalid Input")
except Exception as e:
    print("opps something went wrong")
finally:
    print("resource closed")