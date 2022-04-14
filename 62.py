try:
     a = int(input("enter first number: "))
     b = int(input("enter second number: "))
     result = a / b
     print(result)
except ZeroDivisionError as e:
     print("colud not divide by zero")
except ValueError as e:
    print("one of the variables is not a number")
except BaseException as e:
    print("unknown error:" + str(e.args))
# print("finished")


