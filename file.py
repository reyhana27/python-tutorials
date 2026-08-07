try:
    with open("notes.txt", "r") as f:
        print(f.read())
except:
    print("file no found")
