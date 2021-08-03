def select(memory):

    s = memory.split(", ")
    result = memory.split(", ")

    set1 = set()

    for i in range(len(s)):

        if s[i].find('!') != -1:
            set1.add(str(s[i])[(s[i].find('!') + 1):len(s[i])])
            if i != len(s) - 1:
                set1.add(str(s[i + 1])[(s[i + 1].find('!') + 1):len(s[i + 1])])

    for i in s:
        for j in set1:
            if i.find(j) != -1:
                result.remove(i)

    return ', '.join(result)
