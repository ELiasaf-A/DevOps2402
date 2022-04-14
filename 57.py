def get_name():
    current_name = input("enter your name: ")
    my_file = open("names.txt", "a")
        my_file.write("eliasaf\nmoshhe\ndorr\n")
    my_file.close()

def show_name():
    my_file = open("names.txt")
    for name in my_file.readlines():
    print(f"heloo {name}")

