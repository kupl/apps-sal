# def my_languages(results):
#     ans = []
#     for i in results:
#         a = results.values()
# #         if a > 60:
# #             ans.append(a)
#         print(a)

def my_languages(results):
    dgu = sorted(list(results.items()), key=lambda x: x[1], reverse=True)
    a = []
    for i in dgu:
        li = list(i)
        if li[1] >= 60:
            for u in li:
                if isinstance(u, str):
                    a.append(u)
    return a


#         print(i)
