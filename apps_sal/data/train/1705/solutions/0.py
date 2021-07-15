def spidey_swings(building_params):
    buildings = get_buildings(building_params)
    end_position = get_total_length(buildings)
    latch_positions = []
    jump_position = 0
    while is_not_possible_to_reach_the_end(buildings, jump_position, end_position):
        candidate_jumps = [
            building.get_variables_for_max_displacement(jump_position)
            for building in buildings
            if building.is_reachable(jump_position)
        ]
        candidate_jumps.sort(reverse=True)
        _, latch_position, jump_position = candidate_jumps[0]
        latch_positions.append(latch_position)

    candidate_final_jumps = [
        building.get_variables_aiming_end(jump_position, end_position)
        for building in buildings
        if (building.is_reachable(jump_position) and
            building.is_possible_to_reach_the_end(jump_position, end_position))
    ]
    candidate_final_jumps.sort(reverse=True)
    _, latch_position = candidate_final_jumps[0]
    latch_positions.append(latch_position)

    return latch_positions


def get_buildings(building_params):
    pos = 0
    buildings = []
    for (height, width) in building_params:
        building = Building(height, width, pos)
        buildings.append(building)
        pos += width
    return buildings


def get_total_length(buildings):
    return sum(building.width for building in buildings)


def is_not_possible_to_reach_the_end(buildings, jump_position, end_position):
    return not any(building.is_possible_to_reach_the_end(jump_position, end_position)
                   for building in buildings)


class Building:
    def __init__(self, height, width, pos):
        self.height = height
        self.width = width
        self.pos = pos

    def max_rope_length(self):
        return self.height - 20

    def distance_to_rooftop(self):
        return self.height - 50

    def max_horizontal_displacement(self):
        hypotenuse = self.max_rope_length()
        vertical = self.distance_to_rooftop()
        return (hypotenuse ** 2 - vertical ** 2) ** .5

    def latch_pos_for_max_displacement(self, jump_pos):
        if jump_pos < self.pos - self.max_horizontal_displacement():
            return None
        if jump_pos < self.pos + self.width - self.max_horizontal_displacement():
            return int(jump_pos + self.max_horizontal_displacement())
        if jump_pos < self.pos + self.width:
            return int(self.pos + self.width)
        return None

    def rope_length_for_max_displacement(self, jump_pos):
        horizontal = (self.latch_pos_for_max_displacement(jump_pos) - jump_pos)
        vertical = self.distance_to_rooftop()
        return (horizontal ** 2 + vertical ** 2) ** .5

    def advanced_distance_for_max_displacement(self, jump_pos):
        return (self.latch_pos_for_max_displacement(jump_pos) - jump_pos) * 2

    def ratio_max_displacement_rope(self, jump_pos):
        return (self.advanced_distance_for_max_displacement(jump_pos) /
                self.rope_length_for_max_displacement(jump_pos))

    def get_variables_for_max_displacement(self, pos):
        latch_pos = self.latch_pos_for_max_displacement(pos)
        next_jump_pos = pos + self.advanced_distance_for_max_displacement(pos)
        ratio = self.ratio_max_displacement_rope(pos)
        return ratio, latch_pos, next_jump_pos

    def latch_pos_aiming_end(self, jump_pos, end_pos):
        max_latch_pos = (jump_pos + end_pos) / 2
        if jump_pos < self.pos - self.max_horizontal_displacement():
            return None
        if jump_pos <= max_latch_pos:
            max_latch_pos = max(max_latch_pos, self.pos)
            return int(max_latch_pos + .5)
        return None

    def rope_length_aiming_end(self, pos, end_pos):
        horizontal = self.latch_pos_aiming_end(pos, end_pos) - pos
        vertical = self.distance_to_rooftop()
        return (horizontal ** 2 + vertical ** 2) ** .5

    def ratio_aiming_end(self, pos, end_pos):
        horizontal = end_pos - pos
        rope = self.rope_length_aiming_end(pos, end_pos)
        ratio = horizontal / rope
        return ratio

    def get_variables_aiming_end(self, pos, end_pos):
        latch_pos = self.latch_pos_aiming_end(pos, end_pos)
        ratio = self.ratio_aiming_end(pos, end_pos)
        return ratio, latch_pos

    def is_possible_to_reach_the_end(self, pos, end_pos):
        if not self.is_reachable(pos):
            return False
        return pos + self.advanced_distance_for_max_displacement(pos) >= end_pos

    def is_reachable(self, pos):
        return self.latch_pos_for_max_displacement(pos) is not None

