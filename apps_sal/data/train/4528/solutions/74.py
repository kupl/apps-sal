def my_languages(results):
    s2 = []
    s = sorted(list(results.items()), key=lambda x: x[1], reverse=True)
    for i in range(len(s)):
        if s[i][1] >= 60:
            s2.append(s[i][0])
    return s2
