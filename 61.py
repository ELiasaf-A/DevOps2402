try:
     a = int(input("enter first number: "))
     b = int(input("enter second number: "))
     result = a / b
     print(result)
except BaseException as e:
     print("something went wrong:" + str(e.args))
print("finished")


# a = "כלי חדש שיכול לדלג על שגיאות try + except"
# b = "BaseException  nוסף את הודעת שגיאה ומאפשר לי לראות אותה "
# d = e.args " מחיזר לי את הדאטה של השגיאה שלי "

