def capitalize(s, ind):
    news = list(s)
    for i in ind:
        if i <= len(s):
            news[i] = s[i].upper()
    return ''.join(news)
