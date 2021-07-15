def find_page_number(pages):
    n = [1]
    return [i for i in pages if n[-1] != i or n.append(n[-1]+1)]
