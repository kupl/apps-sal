from string import ascii_lowercase, digits

def vowel_start(st): 
    return ''.join([
        (' ' + c) if c in 'aeiou' else c 
        for c in st.lower() 
        if c in ascii_lowercase + digits
    ]).lstrip()
