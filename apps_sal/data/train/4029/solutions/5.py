import re


def search_substr(full_text, search_text, allow_overlap=True):
    if allow_overlap:
        try:
            return len(re.findall(search_text[0] + '(?={})'.format(search_text[1:]), full_text))
        except IndexError:
            return 0
    else:
        return len(re.findall(search_text, full_text)) if search_text else 0
