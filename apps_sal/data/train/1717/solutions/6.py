from operator import itemgetter


def top_3_words(text):
    text0 = "".join([c if c in "abcdefghijklmnopqrstuvwxyz'" else " " for c in text.lower()])
    check_dict = {}
    text0 = text0.split()
    for x in text0:
        if not any(i.isalpha() for i in x):
            text0.pop(text0.index(x))
    for x in text0:
        if x in check_dict:
            check_dict[x] += 1
        else:
            check_dict.update({x: 1})
    top_3_list = list(sorted(list(check_dict.items()), key=itemgetter(1), reverse=True)[:3])
    return list(map(itemgetter(0), top_3_list))
