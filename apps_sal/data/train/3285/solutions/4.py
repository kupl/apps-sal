import re

def trump_detector(trump_speech):
    matches = re.findall(r'([aeiou])(\1*)', trump_speech.lower(), flags=re.I)
    if matches:
        return round(sum(len(m[1]) for m in matches) / len(matches), 2)
    return 0
