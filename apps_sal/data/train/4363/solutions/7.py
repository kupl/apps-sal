def reverser(sentence):
    text = sentence.split(' ')
    ans = []
    for i in text:
        ans.append(i[::-1])
    return ' '.join(ans)
