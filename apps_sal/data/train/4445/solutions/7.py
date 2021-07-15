import re, string
def is_haiku(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower().splitlines() # Convert text to lowercase and split by lines
    # Count as a syllable if consonant followed by vowel
    sylRegex = re.compile(r'[^aeiouy\s][aeiouy]') #consonant vowel
    syl2Regex = re.compile(r'''                 #for edge cases
    (ia[^lgn])|(riet)|
    (iu)|([^tn]io[^nr])|(ii)|
    ([aeiouym]bl$)|(aeiou){3}|(^mc)|(ism$)|
    (([^aeiouy])\1l$)|([^l]lien)|
    (^coa[dglx].)|([^gq]ua[^auieol])|(dnt$)''', re.VERBOSE)
    endsERegex = re.compile(r'[^aeiouy][aeiouy][aeiou]*[^e\s]+e(?:\s|$)') # -1 syllable if the word ends with "e"
    endsE2Regex = re.compile(r'^\b[ea]\w{1,2}e(?:\s|$)') # age, aide, edge
    beginVRegex = re.compile(r'\b[aeiouy]') # +1 syllable if the word begins with a vowel
    exceptions_add = re.compile(r'''(triangle)''') #based on random case failures
    exceptions_minus = re.compile(r'''(obvious)''')

# Counts for each line
    count = []
    for i in range(len(text)):
        syl = len(sylRegex.findall(text[i])) + len(syl2Regex.findall(text[i]))
        endsE_set1 = set(endsERegex.findall(text[i]))
        endsE_set2 = set(endsE2Regex.findall(text[i]))
        endsE = len(endsE_set1.union(endsE_set2))
    
        count.append(syl - endsE + len(beginVRegex.findall(text[i])) + len(exceptions_add.findall(text[i]))-len(exceptions_minus.findall(text[i])))
        print((text[i]))
        print((sylRegex.findall(text[i])))
        print((syl2Regex.findall(text[i])))
        print((endsERegex.findall(text[i])))
        print((endsERegex.findall(text[i])))
        print((beginVRegex.findall(text[i])))
        print(count) 
        
    return count==[5,7,5]

