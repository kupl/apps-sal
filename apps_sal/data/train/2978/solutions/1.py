def count_sel(lst):
    occ = lst.count(sorted(lst, key=lambda x: lst.count(x), reverse=True)[0])
    return [len(lst), len(set(lst)), len([x for x in lst if lst.count(x) == 1]), [sorted(set((x for x in lst if lst.count(x) == occ))), occ]]
