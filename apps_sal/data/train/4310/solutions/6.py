def swap(st):

    for vowel in st:
        if vowel in ('a','e','i','o','u'):
          st = st.replace(vowel, vowel.upper())
          
    return st
