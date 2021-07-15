import re

def pseudo_sort(st):
    lower_case_words = re.findall(r'\b[a-z]\w*', st)
    upper_case_words = re.findall(r'\b[A-Z]\w*', st)

    lower_case_words.sort()
    upper_case_words.sort(reverse=True)

    return ' '.join(lower_case_words + upper_case_words)
