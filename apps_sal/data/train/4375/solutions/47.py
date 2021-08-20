def get_planet_name(id):
    hop = [['Mercury'], ['Venus'], ['Earth'], ['Mars'], ['Jupiter'], ['Saturn'], ['Uranus'], ['Neptune']]
    return "'".join(hop[id - 1])
