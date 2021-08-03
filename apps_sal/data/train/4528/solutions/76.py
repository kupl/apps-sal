def my_languages(results):
    lst = []
    d = {}
    for key, value in results.items():
        if value >= 60:
            d.update({f'{key}': f'{value}'})
    sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in sort_d:
        lst.append(i[0])
    return lst
