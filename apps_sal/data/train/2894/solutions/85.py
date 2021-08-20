def triple_trouble(one, two, three):
    news = ''
    for i in range(0, len(one)):
        news = news + one[i] + two[i] + three[i]
    return news
