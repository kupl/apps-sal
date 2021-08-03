class Solution:
    def odd_cycle_exists(self, person_to_disliked_persons, person_visited, person, level):
        if (person_visited[person]):
            if (level - 1 != person_visited[person]):
                return (level - person_visited[person]) % 2
        else:
            person_visited[person] = level
            level += 1

            for next_person in person_to_disliked_persons[person]:
                if (self.odd_cycle_exists(person_to_disliked_persons, person_visited, next_person, level)):
                    return True

        return False

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        N += 1
        person_visited = [0] * N
        person_to_disliked_persons = [set() for i in range(N)]

        for dislike in dislikes:
            person_to_disliked_persons[dislike[0]].add(dislike[1])
            person_to_disliked_persons[dislike[1]].add(dislike[0])

        for i in range(1, N):
            if (person_visited[i] == 0 and self.odd_cycle_exists(person_to_disliked_persons, person_visited, i, 1)):
                return False

        return True
