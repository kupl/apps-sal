def my_languages(dict):
    store = []
    for key, value in list(dict.items()):
        if value >= 60:
            store.append(key)
    return sorted(store, key=lambda x: dict[x], reverse=True)
