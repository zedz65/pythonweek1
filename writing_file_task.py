file = open("filename.txt", "w")

for n in range(1,11): #for range is set to 1 to 10 starts from 1 finishes 1 before so prints 1 -10
    newline = "This is line" + str(n) + "\n" #will print newline text and puts a space
    file.write(newline) # wrote it to a file called newline
    print(newline) #i printed this so i could see the result
file.close() #close the file

#This will create a file called "filename.txt" and will write 10 lines to it, each line containing the string "This is line" followed by the line number.

#Note, here we make use of the \n in order to move to a new lines after each line is complete.