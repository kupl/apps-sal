def sort_reindeer(reindeer_names):
    sorted_list = []
    for name in reindeer_names:
        sorted_list.append(name.split())
    sorted_list = sorted(sorted_list, key=lambda names: names[1])

    result = []

    for item in sorted_list:
        name = item[0] + ' ' + item[1]
        result.append(name)
    
    return result
