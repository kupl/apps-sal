def nkotb_vs_homie(requirements):
    return ['{}! Homie dont play that!'.format(a[8:-5].title()) for b in requirements for a in b] + ['{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'.format(*(len(x) for x in requirements))]
