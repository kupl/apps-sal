from operator import itemgetter


def top_3_words(text):
    text0 = "".join([c if c in "abcdefghijklmnopqrstuvwxyz'" else " " for c in text.lower()])  # change rubbish to " "
    check_dict = {}  # create dictionary
    text0 = text0.split()  # convert text to a list
    for x in text0:  # remove lone "'"s
        if not any(i.isalpha() for i in x):
            text0.pop(text0.index(x))
    for x in text0:
        if x in check_dict:
            check_dict[x] += 1  # count each use
        else:
            check_dict.update({x: 1})  # create keys and values
    top_3_list = list(sorted(list(check_dict.items()), key=itemgetter(1), reverse=True)[:3])  # sorts
    return list(map(itemgetter(0), top_3_list))  # returns only the word
