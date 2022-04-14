my_file = open("read_my_contenst.txt")
a = my_file.readlines()
for line in a:
    print(line, end='')
