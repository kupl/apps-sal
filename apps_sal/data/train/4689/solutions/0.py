def create_report(names):
    result = {}

    for name in names:
        if name.startswith("Labrador Duck"):
            return ["Disqualified data"]

        name = name.upper().replace("-", " ").split()
        count = int(name.pop())

        if len(name) == 1:
            code = name[0][:6]
        elif len(name) == 2:
            code = name[0][:3] + name[1][:3]
        elif len(name) == 3:
            code = name[0][:2] + name[1][:2] + name[2][:2]
        elif len(name) == 4:
            code = name[0][0] + name[1][0] + name[2][:2] + name[3][:2]

        if code in result:
            result[code] += count
        else:
            result[code] = count

    return sum([[name, result[name]] for name in sorted(result)], [])
