def grabscrab(w, pw):
    return [i for i in pw if all(w.count(j)==i.count(j) for j in w)]
