import operator

def my_languages(dico):
    dico = dict(sorted(dico.items(), key=operator.itemgetter(1),reverse=True))
    return (list(x for x in dico if dico[x] >= 60))
