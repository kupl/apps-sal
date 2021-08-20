import re


def apparently(Q):
    return re.sub('(?<=\\band|\\bbut)\\b(?! apparently\\b)', ' apparently', Q)
