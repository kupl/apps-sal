def nkotb_vs_homie(requirements):
    requirements = list(requirements)
    temp = []
    for i in range(len(requirements)):
        requirements[i] = list(map(lambda x: x.replace('We need ', '').replace(' now!', '').title(), requirements[i]))
        for j in requirements[i]:
            temp.append(j)
    temp = list(map(lambda x: x + '! Homie dont play that!', temp))
    lengths = list(map(lambda x: len(x), requirements))
    lastSentence = '%d monitoring objections, %d automation, %d deployment pipeline, %d cloud, and %d microservices.' % (lengths[0], lengths[1], lengths[2], lengths[3], lengths[4])
    temp.append(lastSentence)
    return temp
