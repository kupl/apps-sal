def search_substr(full_text, search_text, allow_overlap=True):
    if search_text == '':
        return 0
    if allow_overlap:
        return len([1 for i in range(len(full_text)) if full_text.startswith(search_text, i)])
    return full_text.count(search_text)
