def my_languages(results):
    filtered = list([tup for tup in list(results.items()) if tup[1]>= 60])
    def mySort(i):
        return i[1]
    filtered.sort(reverse = True, key=mySort)
    return [i[0] for i in filtered]

