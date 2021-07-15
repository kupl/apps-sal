import math 
def pass_the_bill(total_members, conservative_party_members, reformist_party_members):
    avg = total_members / 2
    count = 0
    if reformist_party_members >= avg: return -1
    while avg >= conservative_party_members:
        count += 1
        conservative_party_members +=1
    return count
