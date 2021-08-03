class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        \"\"\"
          put everyone in an unassigned set
          pick arbitrary unassigned person put them into arbitrary group
            DFS walk dislikes links assigning people to correct group, fail if impossible

          return true if we succeed

          extra space: O(N + dislikes.length)
              O(N)  to store unassigned people
              O(dislikes.length)  to map people to their dislikes
              stack with at most O(dislikes.length)

          time: O(N + dislikes.length)
             O(dislikes.length) walk once to map people to dislikes
                     handle
             O(N) each person added to a group once
             O(dislikes.length) each person's dislikes handled once when they're added to group
p        \"\"\"
        unassigned = set(range(1, N+1))
        personal_dislikes = {}
        def add_dislike(a, b):
            dis = personal_dislikes.get(a, [])
            dis.append(b)
            personal_dislikes[a] = dis

        for [a, b] in dislikes:
            add_dislike(a, b)
            add_dislike(b, a)

        # map members to `True` or `False` to represent two groups
        group = {}
        while len(unassigned) > 0:
            person = unassigned.pop()
            group[person] = True
            if person not in personal_dislikes:
                continue
            stack = [(False, enemy) for enemy in personal_dislikes[person]]
            while stack:
                group_choice, p = stack.pop()
                if p in group:
                    if group[p] != group_choice:
                        return False
                else:
                    group[p] = group_choice
                    unassigned.remove(p)
                    for enemy in personal_dislikes[p]:
                        stack.append( (not group_choice, enemy) )

        return True

