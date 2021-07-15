from itertools import groupby
def trump_detector(trump_speech):
    return round(sum((len("".join(x)))-1 for i,x in groupby(trump_speech.lower()) if i in "aeiou")/len([i for i,_ in groupby(trump_speech.lower()) if i in "aeiou"]),2)
