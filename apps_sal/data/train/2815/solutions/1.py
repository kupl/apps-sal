def compress(sentence):
    memo = {}
    return ''.join(map(str, (memo.setdefault(s, len(memo)) for s in sentence.lower().split())))
