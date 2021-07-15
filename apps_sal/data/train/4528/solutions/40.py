def my_languages(results):
    list_values = list(results.values())
    list_values.sort()
    list_values.reverse()

    final_list = []

    for i in list_values:
        for key, val in tuple(results.items()):
            if val == i and i >= 60:
                final_list.append(key)

    return final_list
