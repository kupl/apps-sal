class Solution:
     def findItinerary(self, tickets):
         """
         :type tickets: List[List[str]]
         :rtype: List[str]
         """
         tickets.sort()
         schedule = {}
         for ticket in reversed(tickets):
             schedule[ticket[0]] = schedule[ticket[0]] + [ticket[1]] if ticket[0] in schedule else [ticket[1]]
         return list(reversed(self.fly(schedule, "JFK")))
         
     def fly(self, schedule, depart):
         route = []
         while depart in schedule and len(schedule[depart]) > 0:
             route += self.fly(schedule, schedule[depart].pop())
         route += [depart]
         return route
