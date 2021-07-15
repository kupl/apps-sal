def domain_name(url):
    if url.startswith('htt'):
        removehttp = url.split('//')
        if removehttp[1].startswith('w'):
            removewww = removehttp[1].split('www.')
            solution = removewww[1].split('.')
            return solution[0]
        else:
            solution = removehttp[1].split('.')
            return solution[0]
    elif url.startswith('w'):
        removewww = url.split('www.')
        solution = removewww[1].split('.')
        return solution[0]
    else:
        solution = url.split('.')
        return solution[0]
