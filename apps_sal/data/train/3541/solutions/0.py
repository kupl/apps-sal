def find_page_number(pages):
    n, miss = 1, []
    for i in pages:
        if i!=n: miss.append(i)
        else:    n+=1
    return miss
