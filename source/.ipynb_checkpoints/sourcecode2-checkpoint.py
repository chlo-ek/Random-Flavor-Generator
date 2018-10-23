myFile = open("spam1.txt")

total = 0
count = 0

for line in myFile:
    readLine = myFile.readline()
    colon = readLine.find(":")
    endSpace = readLine.find(" ", 22)

    num = readLine[colon+2:endSpace]
    num = float(num)
    total = total + num
    
    if num > .9:
        count = count + 1
    
average = total / 500

print("Average: ", average)
print("Number of emails with spam value > .9: ", count)