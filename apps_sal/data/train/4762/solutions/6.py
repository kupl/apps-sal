def nkotb_vs_homie(r):
    output = []
    for req in r:
        for requirement in req:
            require = requirement.split(' ')
            output.append(require[2].capitalize() + '! Homie dont play that!')
    final = str(len(r[0])) + ' monitoring objections, ' \
        + str(len(r[1])) + ' automation, ' \
        + str(len(r[2])) + ' deployment pipeline, ' \
        + str(len(r[3])) + ' cloud, and ' \
        + str(len(r[4])) + ' microservices.'
    output.append(final)
    return output
