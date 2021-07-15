from collections import Counter
from string import ascii_letters, printable

keep = ascii_letters + "'"
remove = printable.translate(str.maketrans('', '', keep))
table = str.maketrans(keep + remove, keep.lower() + ' ' * len(remove))

def top_3_words(text):
    words = (word for word in text.translate(table).split() if set(word) != {"'"})
    return [word for word, freq in Counter(words).most_common(3)]
