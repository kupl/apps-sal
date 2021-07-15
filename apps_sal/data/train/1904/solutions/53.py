import math
class Solution:
    def __init__(self):
        self.dist_coord = dict()
        self.dist_heap = [None]
        self.final_result = list()
        
    def _calc_dist(self, x, y):
        return math.sqrt(x*x + y*y)

    def _calc_dist_coord(self):
        for point in self.coords:
            dist = self._calc_dist(point[0], point[1])
            if self.dist_coord.get(dist) is None:
                self.dist_coord[dist] = [point]
                self.dist_heap.append(dist)
            else:
                self.dist_coord[dist].append(point)
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.coords = points
        self._calc_dist_coord()
        for i in reversed(list(range(1, len(self.dist_heap)//2 + 1))):
            self.shift_down(self.dist_heap, i)
        
        while K > 0 and len(self.dist_heap) > 1:
            # print(self.dist_coord, self.dist_heap)
            for point in self.dist_coord[self.dist_heap[1]]:
                self.final_result.append(point)
                K -= 1
            self.del_elem_from_heap(self.dist_heap)
            # K -= 1
        return self.final_result
            
    def shift_up(self, h_list):
        i = len(h_list) - 1
        while int(i/2) > 0:
            if h_list[i] > h_list[int(i/2)]:
                h_list[i], h_list[int(i/2)] = h_list[int(i/2)], h_list[i]
            i = int(i/2)

    def shift_down(self, h_list, start):
        i = start
        l = 2* i
        r = 2* i + 1
        if l < len(h_list) and h_list[i] > h_list[l]:
            i = l

        if r < len(h_list) and h_list[i] > h_list[r]:
            i = r

        if i != start:
            h_list[start], h_list[i] = h_list[i], h_list[start]
            self.shift_down(h_list, i)

    def add_elem_to_heap(self, h_list, val):
        h_list.append(val)
        self.shift_up(h_list)

    def del_elem_from_heap(self, h_list):
        h_list[1] = h_list[-1]
        h_list.pop()
        self.shift_down(h_list, 1)
        

