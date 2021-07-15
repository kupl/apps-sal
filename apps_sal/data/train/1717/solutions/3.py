from collections import Counter
import re

def top_3_words(text):
    words = re.findall(r"[a-z][a-z']*|[a-z']*[a-z]", text, re.IGNORECASE)
    topchart = Counter([word.lower() for word in words]).most_common(3)
    return [top[0] for top in topchart]
