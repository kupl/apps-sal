from math import ceil

EFF = {
    ('fire','grass'):     2,
    ('fire','water'):    .5,
    ('grass','water'):    2,
    ('electric','water'): 2,
}

def calculate_damage(you, opp, attack, defense):
    k   = (you,opp) if you<opp else (opp,you)
    eff = .5 if you==opp else EFF.get(k,1) if k[0]==you else 1/EFF.get(k,1)
    return ceil( 50 * eff * attack / defense )
