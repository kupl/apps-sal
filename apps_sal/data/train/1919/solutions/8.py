class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        class Vert(object):

            def __init__(self):
                self.visited = 0
                self.adjList = []
                self.invAdjList = []
                self.inDegree = 0
                self.outDegree = 0
        verts = []
        for _ in range(numCourses):
            verts.append(Vert())
        for prereq in prerequisites:
            pre = prereq[1]
            post = prereq[0]
            verts[pre].adjList.append(post)
            verts[pre].outDegree += 1
            verts[post].invAdjList.append(pre)
            verts[post].inDegree += 1
        coursesToLearn = deque()

        def visitCourse(index):
            """verts, coursesToLearn, visited"""
            if verts[index].visited == 2:
                return 0
            elif verts[index].visited == 1:
                return 1
            verts[index].visited = 1
            for i in verts[index].adjList:
                if visitCourse(i) == 1:
                    return 1
            verts[index].visited = 2
            coursesToLearn.appendleft(index)
            return 0
        for i in range(numCourses):
            if verts[i].visited == 0:
                if visitCourse(i) == 1:
                    break
        if len(coursesToLearn) == numCourses:
            return list(coursesToLearn)
        else:
            return []
