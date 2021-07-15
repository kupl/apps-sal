# def my_languages(dict):
#     store = []
#     for key, value in dict.items():
#         if value >= 60:
#             store.append((key, value))
#     store.sort(key=lambda x: x[-1])
#     return [x[0] for x in store]
def my_languages(dict):
    store = []
    for key, value in list(dict.items()):
        if value >= 60:
            store.append(key)
    return sorted(store, key=lambda x: dict[x], reverse= True)
            
        

