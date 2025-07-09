# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        number_of_events = len(events)
        max_day = max(event[1] for event in events)

        events.sort(key=lambda event: (event[0], event[1]))
        
        pq = []
        maximum_events = 0
        i = 0

        for day in range(1, max_day + 1):
            # find all events that start before or equal to current day
            while i < number_of_events and events[i][0] <= day:
                heapq.heappush(pq, events[i][1])
                i += 1
        
            # remove all events that have already ended
            while pq and pq[0] < day:
                heapq.heappop(pq)
            
            # take next event with earliest end day
            if pq:
                heapq.heappop(pq)
                maximum_events += 1

        return maximum_events