import operator


def my_languages(dico):
    return (list(x for x in dict(sorted(list(dico.items()), key=operator.itemgetter(1), reverse=True)) if dict(sorted(list(dico.items()), key=operator.itemgetter(1), reverse=True))[x] >= 60))
