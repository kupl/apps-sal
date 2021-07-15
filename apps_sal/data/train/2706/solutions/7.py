def pass_the_bill(total_members, conservative_party_members, reformist_party_members):
    independants = total_members - conservative_party_members - reformist_party_members
    majority = total_members // 2 + 1
    needed = max(0, majority - conservative_party_members)
    return -1 if needed > independants else needed
