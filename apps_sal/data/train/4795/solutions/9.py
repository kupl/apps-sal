import re
 
def syl_count(word):
    return len(re.findall(r'[aeiou]+', word.lower()))

def flesch_kincaid(text):
    sentences_cnt = len([x for x in re.sub('\.|!|\?', '.', text).split('.') if x != ''])
    words_cnt = float(text.count(' ') + 1);
    syl_cnt = 0.0;
    for word in text.split(' '):
        syl_cnt += syl_count(word);
    syl_cnt /= words_cnt
    return round((0.39 * words_cnt / sentences_cnt) + (11.8 * syl_cnt) - 15.59, 2)

