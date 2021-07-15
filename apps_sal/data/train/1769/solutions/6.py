
def shortestPath(topology, startPoint, endPoint):
    '''
    Problem description: https://www.codewars.com/kata/5709aa85fe2d012f1d00169c/train/python
    Made intentionally with 2 classes: PathFinder and TimeFinder
    For simulating real-life project structure, covering unittests, multiprocessing etc.
    '''

    class PathFinder:
        def __init__(self, topology, start_point, end_point):
            self.start_point = start_point
            self.end_point = end_point
            self.tplg = topology

            self.next_step = None
            self.considered_path = None
            self.backtrack = [{self.start_point: [*self.tplg[self.start_point].keys()]}]
            self.history = self.start_point
            self.finished_paths = []

        def solve(self):

            def try_forward():
                get_next_step()
                self.considered_path = self.history + self.next_step

                if self.next_step == self.end_point:
                    self.finished_paths.append(self.considered_path)
                    try_backward()
                elif self.next_step not in self.history:
                    clean_backtrack()
                    add_new_crossroad_to_backtrack()
                    self.history = self.considered_path
                    try_forward()
                else:
                    try_backward()

            def try_backward():
                clean_backtrack()
                try_forward()

            def clean_backtrack():
                del list(self.backtrack[-1].values())[0][-1]
                directions_left_to_consider_at_last_path = list(self.backtrack[-1].values())[0]
                last_path = [*self.backtrack[-1].keys()][0]
                if not directions_left_to_consider_at_last_path and len(last_path) > 1:
                    del self.backtrack[-1]
                    last_path = [*self.backtrack[-1].keys()][0]
                    self.history = last_path

            def add_new_crossroad_to_backtrack():
                self.backtrack.append({self.considered_path: [*self.tplg[self.next_step].keys()]})

            def get_next_step():
                self.next_step = list(self.backtrack[-1].values())[0][-1]

            def execute():
                try:
                    try_forward()
                except IndexError:
                    pass

            execute()
            return self.finished_paths


    def compute_path_time(path):
        '''Computes time for given path after its validated in PathFinder'''
        def get_time(previous_step, next_step):
            return topology[previous_step][next_step]
        def get_next_pair_of_steps(path, iter_no):
            return path[iter_no], path[iter_no+1]

        time = 0
        for iter_no in range(len(path)-1):
            time += get_time(*get_next_pair_of_steps(path, iter_no))
        return time

    finished_paths = PathFinder(topology, startPoint, endPoint).solve()
    path_time_dict = {path: compute_path_time(path) for path in finished_paths}

    def adjust_for_codewars_requirements(path_time_dict):
        '''
        1. Return list of lists containing waypoints
        2. If 2 paths are equally time consuming, then pick the one with fewer waypoints
        3. If there are still multiple solutions complying with 2nd requirement, sort them in alphabetical order
        '''
        shortest_time = min(path_time_dict.values())
        paths_with_shortest_time = [path for path in path_time_dict.keys() if path_time_dict[path]==shortest_time]
        minimum_waypoint_number = min([len(path) for path in paths_with_shortest_time])
        paths_with_minimum_waypoint_number = list(filter(lambda x: len(x) == minimum_waypoint_number, paths_with_shortest_time))
        adjusted = [[waypoint for waypoint in path] for path in sorted(paths_with_minimum_waypoint_number)]
        return adjusted

    return adjust_for_codewars_requirements(path_time_dict)
