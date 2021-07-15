import re

def flesch_kincaid(text):
    sen_l = re.split('[.!?]', text)
    words, syllables, sentences = 0, 0, len(sen_l)-1
    for sen in sen_l[:-1]:
        for w in sen.split():
            words += 1
            syllables += len(re.findall(r'[aeiouAEIOU]+',w))
    return round(0.39*words/sentences+11.8*syllables/words-15.59, 2)

