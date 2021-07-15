import re

def gym_slang(phrase):
    phrase = re.sub(r'([pP])robably', r'\1rolly', phrase)
    phrase = re.sub(r'([iI]) am', r"\1'm", phrase)
    phrase = re.sub(r'([iI])nstagram', r'\1nsta', phrase)
    phrase = re.sub(r'([dD])o not', r"\1on't", phrase)
    phrase = re.sub(r'([gG])oing to', r'\1onna', phrase)
    phrase = re.sub(r'([cC])ombination', r'\1ombo', phrase)
    
    return phrase
