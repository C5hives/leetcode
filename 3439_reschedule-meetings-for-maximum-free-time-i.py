# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        chunks = []
        time = 0
        meeting_index = 0

        # append first chunk if there is free time before the first meeting
        chunks.append(startTime[meeting_index] - time)

        # append chunks between meetings
        for i in range(len(endTime)):
            if i + 1 >= len(startTime):
                break
            chunks.append(startTime[i + 1] - endTime[i])
        
        # append last chunk if there is free time after the last meeting
        chunks.append(eventTime - endTime[-1])
            
        # compute sum of first window of size k + 1
        window_sum = sum(chunks[:k + 1])
        max_sum = window_sum

        # compute the sums of remaining windows
        for i in range(1, len(chunks) - k):
            window_sum = window_sum - chunks[i - 1] + chunks[i + k]
            max_sum = max(window_sum, max_sum)

        return max_sum