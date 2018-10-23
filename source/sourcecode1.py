myFile = open("spam2.txt")

total = 0
count = 0
average = 0

for line in myFile:
    
    if line.find("From ") >= 0:
        startEmail = line.find(" ")
        endEmail = line.find(" ", startEmail + 1)
        fromEmail = line[startEmail:endEmail]
    
    if line.find("To") >= 0:
        startEmail = line.find(" ")
        endEmail = line.find(" ", startEmail + 1)
        toEmail = line[startEmail:endEmail]
        
    if line.find("X-DSPAM-Confidence") >= 0:
        startConfidence = line.find(" ")
        endConfidence = len(line)
        num = line[startConfidence:endConfidence - 1]
        num = float(num)
        
        total = total + num
        count = count + 1
        
        if (num > 0.9):
            print("From = ", fromEmail)
            print("To = ", toEmail)
            
average = total / count
print("Average: ", average)