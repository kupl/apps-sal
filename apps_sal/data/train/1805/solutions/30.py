class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        visited.add(id)
        frequency = {}
        dictionary = {}
        q = deque()
        q.append(id)
        running_level = 1
        solution = []

        while q and running_level <= level:
            length = len(q)

            for index in range(length):
                node = q.popleft()

                for friend in friends[node]:
                    if friend in visited:
                        continue
                    visited.add(friend)

                    if running_level == level:
                        for movie in watchedVideos[friend]:
                            frequency[movie] = frequency.get(movie, 0) + 1
                    else:
                        q.append(friend)

            running_level += 1

        order = set(sorted(frequency.values()))

        for key in frequency:
            dictionary[frequency[key]] = dictionary.get(frequency[key], []) + [key]

        for rank in order:
            solution.extend(sorted(dictionary[rank]))

        return solution
