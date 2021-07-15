def group_cities(seq): 
    result = []
    for element in sorted(list(dict.fromkeys(seq)), key=str.lower):
        for group in result:
            if element.lower() in [group[0].lower()[r:] + group[0].lower()[:r] for r in range(len(group[0].lower()))]:
                group.append(element)
                break
        else:
            result.append([element])

    return sorted(result, key=len, reverse=True)

