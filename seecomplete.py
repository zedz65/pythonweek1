def SEE1(word,phrase):
    phraselist = phrase.split()
    #lenphrase = len(phraselist) dont need it
    count = 0
    for string in phraselist:
        if string == word:
            count = count +1
            
    return count

print(SEE1("hi","hi hello hi hi hi hi ello"))