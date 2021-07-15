class Player:
    def __init__ (self):
        self.red_cards = 0
        self.yellow_cards = 0
    @property
    def excluded (self):
        return (self.red_cards or 
                self.yellow_cards > 1)
    def receive_red (self):
        self.red_cards += 1
    def receive_yellow (self):
        self.yellow_cards += 1

class Team:
    def __init__ (self, size):
        self.size = size
        self.players = {number: Player()
            for number in range(1, size+1)}
    @property
    def count (self):
        return sum(not player.excluded for 
            player in list(self.players.values()))
    def give_red (self, number):
        self.players[number].receive_red()
    def give_yellow (self, number):
        self.players[number].receive_yellow()

def men_still_standing (cards):
    teams = { 'A': Team(11), 'B': Team(11) }
    actions = {
        'R': Team.give_red, 'Y': Team.give_yellow }
    
    import re
    pattern = '(A|B)([0-9]+)(R|Y)'
    for card in cards:
        match = re.match(pattern, card)
        team, player, color = match.group(1, 2, 3)
        actions[color](teams[team], int(player))
        if any(team.count < 7 
               for team in list(teams.values())):
            break
    
    return tuple(team.count for team in list(teams.values()))
        
    
    
    

