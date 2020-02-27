isbn = input("enter isbn: ")
even = 0
odd = 0
for i in range (1,12,2):
    even = even+3*int(isbn[i])
for i in range (0,12,2):
    odd = odd +int(isbn[i])

lastdig = 10-(odd+even)%10
print(lastdig)