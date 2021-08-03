import re


def nkotb_vs_homie(requirements):
    return ['{}! Homie dont play that!'.format(s[8:-5].capitalize()) for r in requirements for s in r]\
        + ['{} monitoring objections, {} automation, {} deployment pipeline, {} cloud, and {} microservices.'.format(*map(len, requirements))]
