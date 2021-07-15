TOTAL =  '{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'

def nkotb_vs_homie(r):
    result = []
    for req in sum(r, []):
        homie = req.split()[2].title()
        result.append(f'{homie}! Homie dont play that!')
    result.append(TOTAL.format(*map(len, r)))
    return result
