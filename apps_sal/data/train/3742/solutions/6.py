def modes(data):
    dict = {i: data.count(i) for i in data}
    if max(dict.values()) != min(dict.values()):
        return sorted([key for (key, value) in dict.items() if value == max(dict.values())])
    return []
