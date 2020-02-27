bio = float(input("input biology"))
chem = float(input("input chemistry"))
phy = float(input("input physics"))
score = (bio+chem+phy)/3

if score >= 40:
    print("you have passed")

else: 
    print("you have failed")