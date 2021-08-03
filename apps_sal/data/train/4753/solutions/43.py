geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds): return [non_geese for non_geese in birds if non_geese not in geese]
