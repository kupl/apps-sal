def remove(text, what):
    for i in what.keys():
        text=text.replace(i,'',what[i])
    return text
