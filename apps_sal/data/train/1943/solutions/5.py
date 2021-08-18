class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        state = [False, False]
        A_index = [0, 0]
        B_index = [0, 0]
        result = []

        def get_event(events, index):
            if index[0] >= len(events):
                return -1
            return events[index[0]][index[1]]
        while True:
            event_a = get_event(A, A_index), A_index[1]
            event_b = get_event(B, B_index), B_index[1]
            if event_a[0] < 0 or event_b[0] < 0:
                break
            event = min(event_a[0], event_b[0])
            is_already_in_progress = all(state)
            if event_a < event_b:
                if A_index[1] == 0:
                    state[0] = 1
                    A_index[1] = 1
                else:
                    state[0] = 0
                    A_index[0] += 1
                    A_index[1] = 0
            else:
                if B_index[1] == 0:
                    state[1] = 1
                    B_index[1] = 1
                else:
                    state[1] = 0
                    B_index[0] += 1
                    B_index[1] = 0
            if is_already_in_progress:
                result[-1][1] = event
            elif all(state):
                result.append([event, -1])
        return result
