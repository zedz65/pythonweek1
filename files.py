file = open("filename.txt", "r") #opens filename.txt in read only

print(file.readline()) #reads first line and prints goes to next
file.readline() # reads next line but doesnt print
print(file.readline()) #prints and reads this line so line 1 and 3 printed
file.seek(0) # navigates to charecter 0 so back to first line
print(file.readline()) # reads the first line again because we seeked 0 first

file.close() # closes file