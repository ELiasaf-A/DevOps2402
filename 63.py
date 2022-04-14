def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age can't be negative")
try:
    get_age()
except ValueError as e:
    print(e.args[0])



# a = raise "המילה הזו מאפשרת לי להקפיץ הודעה שגיאה שלי "
