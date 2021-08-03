import re
base = "too?|fore?|oo|be|are|you|please|people|really|have|know|s|[.,']".split('|')
noob = "2|4|00|b|r|u|plz|ppl|rly|haz|no|z|".split('|')


def n00bify(text):
    for b, n in zip(base, noob):
        def keep_casing(m): return n.upper() if m.group().isupper() else n
        text = re.sub(b, keep_casing, text, flags=re.I)
    if not text:
        return ''
    if text[0] in 'hH':
        text = text.upper()
    if text[0] in 'wW':
        text = 'LOL ' + text
    if len(re.sub('[!?]', '', text)) >= 32:
        text = re.sub('\A(LOL |)', r'\1OMG ', text)
    text = re.sub('([?!])', r'\1' * len(text.split()), text).replace('!!', '!1')
    return ' '.join(w.upper() if i % 2 else w for i, w in enumerate(text.split()))
