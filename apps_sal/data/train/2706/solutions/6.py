import math

def pass_the_bill(total_members, conservative_party_members, reformist_party_members):
    if reformist_party_members >= total_members / 2: return -1
    return max(0, math.ceil(total_members / 2 + .5) - conservative_party_members)
