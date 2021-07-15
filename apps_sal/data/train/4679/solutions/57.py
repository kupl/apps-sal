def to_freud(sentence):
    try:
        res = []
        for i in range(len(sentence.split())):
            res.append('sex')
        return ' '.join(res)
    except:
        return ''
