def my_languages(results):
    array_list = []
    sorted_results = (sorted(list(results.items()), key=lambda k: k[1], reverse=True))
    for i in sorted_results:
        if i[1] >= 60:
            array_list.append(i[0])
    return array_list
