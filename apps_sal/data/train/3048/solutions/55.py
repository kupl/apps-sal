def alternateCase(s):
    news = []
    for i in range(len(s)):
        if s[i].islower():
            news.append(s[i].upper())
        else:
            news += s[i].lower()
    return ''.join(news)
