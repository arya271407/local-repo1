try:
    a=int(input("enter  first number"))
    b=int(input("enter  second number"))
    print(f"before swapping :a={a},b={b}")
    a,b=b,a
    print(f"after swapping:a={a},b={b}")
except ValueError:
   print("plese enter the valid digits")
