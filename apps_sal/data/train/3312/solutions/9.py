# METHOD ONE ~ list comprehension
"100 seconds per 1000 runs of Lorem Ipsum"
# def anagram_counter(s):
#     return sum([1for i,c in enumerate(s)for w in s[i+1:]if sorted(c)==sorted(w)])

# METHOD TWO ~ standard iteration
"50 seconds per 1000 runs of Lorem Ipsum"
#def anagram_counter(words):
#    anagram_count = 0
#    for i, current in enumerate(words):#                    FUN FACT:
#        cenrrtu = sorted(current)
#        for word in words[i+1:]:
#            if cenrrtu == sorted(word):#     Lorum Ipsum contains 6,862 anagram matches
#                anagram_count += 1
#    return anagram_count

# METHOD THREE ~ comparing sets to counts
"0.5 seconds per 1000 runs of Lorem Ipsum"
def run_down(number):
    count = 0
    while number:
        count += number - 1
        number -= 1
    return count

def anagram_counter(words):
    sorts = list(''.join(sorted(word)) for word in words)
    unique = set(sorts)
    return sum(run_down(sorts.count(word)) for word in unique)
    
"""
iterations     _comp_    _iter_    _sets_
1              0.0990    0.0541    0.0008
10             1.0113    0.4954    0.0054
100            9.9280    4.8606    0.0535
1000         101.2153   50.2576    0.5660
"""
