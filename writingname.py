name = input("Enter your name: ")

try:
    with open("names.txt", "w") as f:
        f.write(name)
    print("worked")
except:
    print("error")
