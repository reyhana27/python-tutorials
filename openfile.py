file = input("enter filename: ")

try:
    with open(file, "r") as f:
        print(f.read())
except:
    print("file cannot be opened")
