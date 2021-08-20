res1 = '{}! Homie dont play that!'.format
res2 = '{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'.format
get = __import__('re').compile('We need (\\w+) now!').search


def nkotb_vs_homie(requirements):
    return [res1(get(req).group(1).capitalize()) for reqs in requirements for req in reqs] + [res2(*map(len, requirements))]
