file = open("filename.txt", "r") #opens in read only
lines = file.readlines() #reads alllines and stores in variable lines
print(lines) #prints variable line
file.close()# closes file