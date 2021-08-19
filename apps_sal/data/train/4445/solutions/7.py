import re
import string


def is_haiku(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower().splitlines()
    sylRegex = re.compile('[^aeiouy\\s][aeiouy]')
    syl2Regex = re.compile('                 #for edge cases\n    (ia[^lgn])|(riet)|\n    (iu)|([^tn]io[^nr])|(ii)|\n    ([aeiouym]bl$)|(aeiou){3}|(^mc)|(ism$)|\n    (([^aeiouy])\\1l$)|([^l]lien)|\n    (^coa[dglx].)|([^gq]ua[^auieol])|(dnt$)', re.VERBOSE)
    endsERegex = re.compile('[^aeiouy][aeiouy][aeiou]*[^e\\s]+e(?:\\s|$)')
    endsE2Regex = re.compile('^\\b[ea]\\w{1,2}e(?:\\s|$)')
    beginVRegex = re.compile('\\b[aeiouy]')
    exceptions_add = re.compile('(triangle)')
    exceptions_minus = re.compile('(obvious)')
    count = []
    for i in range(len(text)):
        syl = len(sylRegex.findall(text[i])) + len(syl2Regex.findall(text[i]))
        endsE_set1 = set(endsERegex.findall(text[i]))
        endsE_set2 = set(endsE2Regex.findall(text[i]))
        endsE = len(endsE_set1.union(endsE_set2))
        count.append(syl - endsE + len(beginVRegex.findall(text[i])) + len(exceptions_add.findall(text[i])) - len(exceptions_minus.findall(text[i])))
        print(text[i])
        print(sylRegex.findall(text[i]))
        print(syl2Regex.findall(text[i]))
        print(endsERegex.findall(text[i]))
        print(endsERegex.findall(text[i]))
        print(beginVRegex.findall(text[i]))
        print(count)
    return count == [5, 7, 5]
