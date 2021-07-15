def nkotb_vs_homie(requirements):
    res = []
    for arr in requirements: 
        for item in arr: 
            aux = item[8: -5].title()
            res.append('{}! Homie dont play that!'.format(aux))
    res.append('{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'.format(*map(len, requirements)))
    return res
