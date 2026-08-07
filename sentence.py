sentence = input("enter a sentence: ")

try:
    with open("diary.txt", "a") as f:
        f.write(sentence )
    print("done")
except:
    print(error)
