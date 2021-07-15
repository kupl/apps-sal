class TrafficUnit:

    def __init__(self, color):
        # '.': road
        # 'R'/'G'/'B': light
        self.color = color
        self.t = 0

    def can_pass(self):
        return self.color is '.' or self.color == 'G'

    def step(self):
        self.t = (self.t + 1) % 5
        if self.color == 'G':
            if self.t == 0:
                self.color = 'O'
        elif self.color == 'O':
            self.color = 'R'
            self.t = 0
        elif self.color == 'R':
            if self.t == 0:
                self.color = 'G'
        return self

    def __str__(self):
        return self.color


def traffic_lights(road, n):
    def f():
        car_pos = 0
        units = [TrafficUnit(c.replace('C', '.')) for c in road + '.']
        for i in range(n+1):
            xs = list(map(str, units))
            if car_pos < len(road):
                xs[car_pos] = 'C'
            yield ''.join(xs[:-1])
            units = [unit.step() for unit in units]
            if car_pos < len(road) and units[car_pos+1].can_pass():
                car_pos += 1
    return list(f())
