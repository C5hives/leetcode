# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda event: (event[0], event[1]))
        memo = {}
        self.helper(memo, events, 0, k)
        return memo[(0, k)] if (0, k) in memo else 0

    def helper(self, memo, events, current_index, current_k):
        if current_k < 1 or current_index >= len(events):
            return 0
        
        if (current_index, current_k) in memo:
            return memo[(current_index, current_k)]
        
        # attend event
        end_day = events[current_index][1]
        # binary search for the next event that can be attended
        next_index = self.binary_search(events, current_index, end_day)
        value_if_attended = events[current_index][2] + self.helper(memo, events, next_index, current_k - 1)

        # skip event
        value_if_skipped = self.helper(memo, events, current_index + 1, current_k)

        memo[(current_index, current_k)] = max(value_if_skipped, value_if_attended)
        return memo[(current_index, current_k)]

    def binary_search(self, events, start, end_day):
        end = len(events) - 1
        while start < end:
            mid = (start + end) // 2
            if events[mid][0] <= end_day:
                start = mid + 1
            else:
                end = mid
        if events[start][0] <= end_day:
            return len(events)
        return start