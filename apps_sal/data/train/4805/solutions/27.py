def check(wordlist, elem):
    if elem in wordlist:        
        return True
    else:
        return False

print(check(["when's", "the", "next", "Katathon?", 9, 7], "Kaathon?"))
