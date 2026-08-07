while True:
    print("1. write text to a file")
    print("2. read the contents of the file")
    print("3. append new text to the file")
    print("4. exit the program")
    
    choice = input("enter your choice 1, 2, 3, or, 4: ")
    
    try:
        if choice == "1":
            text = input("enter a text: ")
            with open("random.txt", "w") as f:
                f.write(text)
            print("the text is written")
            
        elif choice == "2":
            try:
                with open("random.txt", "r", encoding="UTF8") as f:
                    print(f.read())
            except FileNotFoundError:
                print("file doesnt exist")
        
        elif choice == "3":
            try:
                with open("random.txt", "a") as f:
                    text = input("enter a text: ")
                    f.write(text)
                print("done")
            except FileNotFoundError:
                print("file doesnt exist")
                
        elif choice == "4":
            print("program exitted")
            break
        
        else:
            print("invalid")
    except:
        print("error")
        
