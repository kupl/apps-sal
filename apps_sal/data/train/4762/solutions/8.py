def nkotb_vs_homie(requirements):
    r = []
    c = []
    for reqs in requirements:
        for req in reqs:
            r.append(req.split(' ')[2].title() + '! Homie dont play that!')
        c.append(len(reqs))
    r.append('{0[0]} monitoring objections, {0[1]} automation, {0[2]} deployment pipeline, {0[3]} cloud, and {0[4]} microservices.'.format(c))
    return r
