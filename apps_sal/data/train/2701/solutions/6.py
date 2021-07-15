class Score:
    def __init__(self):
        self.default = {'points': tuple([40, 100, 300, 1200]),'line': int(10)}
        self.current = {'level': int(1), 'lines': int(0), 'point': int(0), 'new_line': int(0)}

    def line__(self):
        self.current['lines'] += self.current['new_line'] 
        if self.current['lines'] >= self.default['line']:
            self.current['level'] += 1
            self.current['lines'] -= self.default['line']
            
    def points__(self):
        self.current['point'] = self.default['points'][self.current['new_line']-1] * (self.current['level'])
    
    def update__(self, current) -> int:
        self.current['new_line'] = current
        self.points__()
        self.line__()
        return self.current['point']

def get_score(arr) -> int:
    score = Score()
    return sum([(score.update__(current)) for current in arr if (current > 0 & current <= 4)])
