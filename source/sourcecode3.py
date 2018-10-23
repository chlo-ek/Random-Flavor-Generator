while True:
    
    try:
        myFile = input("Enter filename: ")
        newFile = open(myFile)
        for line in newFile:
            print(line)
        break

    except:
        print("Error, try again!")