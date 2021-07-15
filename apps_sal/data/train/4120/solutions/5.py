def sort_dict(d):
    import operator
    return sorted(d.items(), key=operator.itemgetter(1), reverse=True)
