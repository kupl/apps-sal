import re
def search_substr(full_text, search_text, allow_overlap=True):
    if not full_text or not search_text: return 0
    if allow_overlap == False: return len(re.findall(r'(' + search_text + ')', full_text))
    else: return len(re.findall(r'(?=(' + search_text + '))', full_text))
