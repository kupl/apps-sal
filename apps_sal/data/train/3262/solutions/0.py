def group_cities(seq):
    result = []
    sort_result =[]
    seq = list(dict.fromkeys(seq)) #removing  duplicates
    for e, i in enumerate(seq):
        sort_result = [j for j in seq if len(j)==len(i) and j.lower() in 2*(i.lower())]
        if not sorted(sort_result) in result :
            result.append(sorted(sort_result))
    return(sorted(sorted(result),key=len,reverse=True))
