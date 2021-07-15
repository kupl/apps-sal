Kind_sperm = {'XY':"Congratulations! You're going to have a son.",\
    'XX':"Congratulations! You're going to have a daughter."}
def chromosome_check(sperm):
    if sperm in Kind_sperm.keys():
        return Kind_sperm[sperm]
