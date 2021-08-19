import re


def contamination(text, char):
    if text == '' or char == '':
        return ''
    else:
        contaminated_word = re.sub('[!#~@$%&*_+{}|:"<>;,/?=a-zA-Z0-9]', char, text)
        return contaminated_word
