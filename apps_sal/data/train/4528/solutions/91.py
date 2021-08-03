def my_languages(results):
    l = sorted(list(results.items()), key=lambda x: x[1], reverse=True)
    ll = []
    for i in l:
        if results.get(i[0]) >= 60:
            ll.append(i[0])
    return ll
