from collections import OrderedDict


class TowerDefense:

    def __init__(self, grid, turrets, aliens):
        """ Create dictionary for turrets (using name) and lists with path and aliens """
        self._turrets = OrderedDict()
        self._path = []
        self._n = len(grid)
        grid_str = ''.join(grid)
        self._determine_turret_positions(turrets, grid_str)
        self._determine_path_and_guarded_positions(grid_str)
        self._aliens = aliens

    def _determine_turret_positions(self, turrets, grid_str):
        """ Add turrets in sorted order to dictionary """
        for (turret, settings) in sorted(turrets.items()):
            ind = grid_str.find(turret)
            x = ind % self._n
            y = ind // self._n
            self._turrets[turret] = {'pos': (x, y), 'range2': settings[0] ** 2, 'shots': settings[1], 'guards': []}

    def _determine_path_and_guarded_positions(self, grid_str):
        """ Find all positions of the path and determine which once can be reached by the turrets """
        ind_0 = grid_str.find('0')
        x = ind_0 % self._n
        y = ind_0 // self._n
        self._add_point_to_path_and_guarded_list((x, y))
        next_point = self._get_next_point_on_path(grid_str)
        while next_point:
            self._add_point_to_path_and_guarded_list(next_point)
            next_point = self._get_next_point_on_path(grid_str)

    def _add_point_to_path_and_guarded_list(self, point):
        """ Add the point to the path list and to any turrets that can reach it """
        self._path.append(point)
        self._add_to_guarded_list(point)

    def _get_next_point_on_path(self, grid_str):
        """ Based on the last point on the path, get the adjacent path point that is not yet on the path """
        (curr_x, curr_y) = self._path[-1]
        if curr_x > 0:
            test_x = curr_x - 1
            test_y = curr_y
            ind = test_x + self._n * test_y
            if grid_str[ind] == '1' and (not (test_x, test_y) in self._path):
                return (test_x, test_y)
        if curr_x < self._n - 1:
            test_x = curr_x + 1
            test_y = curr_y
            ind = test_x + self._n * test_y
            if grid_str[ind] == '1' and (not (test_x, test_y) in self._path):
                return (test_x, test_y)
        if curr_y > 0:
            test_x = curr_x
            test_y = curr_y - 1
            ind = test_x + self._n * test_y
            if grid_str[ind] == '1' and (not (test_x, test_y) in self._path):
                return (test_x, test_y)
        if curr_y < self._n - 1:
            test_x = curr_x
            test_y = curr_y + 1
            ind = test_x + self._n * test_y
            if grid_str[ind] == '1' and (not (test_x, test_y) in self._path):
                return (test_x, test_y)
        return None

    def _add_to_guarded_list(self, point):
        """ Add point to list of guarded poisitions, if it is within turret range """
        for (turret, settings) in self._turrets.items():
            if (point[0] - settings['pos'][0]) ** 2 + (point[1] - settings['pos'][1]) ** 2 <= settings['range2']:
                settings['guards'].insert(0, point)

    def aliens_that_pass_the_turrets(self):
        """ Determine the number of aliens that pass the turrets """
        total_turns = len(self._path) + len(self._aliens)
        for turn in range(1, total_turns + 1):
            total_remaining = 0
            for turret in self._turrets:
                self._turrets[turret]['remaining'] = self._turrets[turret]['shots']
                total_remaining += self._turrets[turret]['remaining']
            alien_pos_ind = {}
            for it in range(turn):
                if it < len(self._aliens) and turn - 1 - it < len(self._path):
                    alien_pos_ind[self._path[turn - 1 - it]] = it
            while total_remaining > 0:
                for turret in self._turrets:
                    if self._turrets[turret]['remaining'] > 0:
                        for pos in self._turrets[turret]['guards']:
                            if pos in alien_pos_ind and self._aliens[alien_pos_ind[pos]] > 0:
                                total_remaining -= 1
                                self._turrets[turret]['remaining'] -= 1
                                self._aliens[alien_pos_ind[pos]] -= 1
                                break
                        else:
                            total_remaining -= self._turrets[turret]['remaining']
                            self._turrets[turret]['remaining'] = 0
        return sum(self._aliens)

    def print_map(self, turn=0):
        """ Print a map of the current turn with path, alien strength, and turrets """
        turret_pos = {}
        for (turret, settings) in self._turrets.items():
            turret_pos[settings['pos']] = turret
        alien_pos = {}
        for it in range(turn):
            if it < len(self._aliens) and turn - 1 - it < len(self._path):
                alien_pos[self._path[turn - 1 - it]] = self._aliens[it]
        for y in range(self._n):
            for x in range(self._n):
                if (x, y) in alien_pos:
                    print('%02i' % alien_pos[x, y], end=' ')
                elif (x, y) in self._path:
                    print('XX', end=' ')
                elif (x, y) in turret_pos:
                    print(2 * turret_pos[x, y], end=' ')
                else:
                    print('  ', end=' ')
            print('\n')


def tower_defense(grid, turrets, aliens):
    td = TowerDefense(grid, turrets, aliens)
    return td.aliens_that_pass_the_turrets()
