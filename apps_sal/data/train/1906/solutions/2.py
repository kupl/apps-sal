class Solution:

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        ordered_line = []
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        for person in people:
            ordered_line.insert(person[1], person)
        return ordered_line
