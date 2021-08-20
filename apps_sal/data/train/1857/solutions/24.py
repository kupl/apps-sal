class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        all_possible_seats = [set([2, 3, 4, 5]), set([4, 5, 6, 7]), set([6, 7, 8, 9])]
        seat_map = collections.defaultdict(set)
        for s in reservedSeats:
            seat_map[s[0]].add(s[1])
        count = 0
        for row in seat_map:
            seats_taken = seat_map[row]
            for cand in all_possible_seats:
                if not cand.intersection(seats_taken):
                    count += 1
                    seats_taken = cand.union(seats_taken)
        return count + 2 * (n - len(seat_map.keys()))
