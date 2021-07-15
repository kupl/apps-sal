def to_freud(sentence):
    sent=sentence.split()
    ans=''
    for i in sent:
        ans=ans+'sex '
    return ans[:len(ans)-1]

