class Solution:
    def numRabbits(self, answers):
        if not answers:
            return 0

        answers.sort()
        ht = dict(list(zip(list(set(answers)), [0] * len(set(answers)))))
        for e in answers:
            ht[e] += 1

        min_count = 0
        for e in set(answers):
            group, count = e, ht[e]

            if count <= group + 1:
                min_count += group + 1
            else:
                # apply pigeonhole principle
                a, b = divmod(count, group + 1)
                min_count += (a + (b > 0)) * (group + 1)

        return min_count
