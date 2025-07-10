# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

import bisect

class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        chunks = []
        time = 0
        meeting_index = 0

        chunks = []
        gap_left = startTime[meeting_index] - time
        if len(startTime) == 0:
            return eventTime - (endTime[0] - startTime[0])
        gap_right = startTime[meeting_index + 1] - endTime[meeting_index]
        chunks.append((gap_left, endTime[0] - startTime[0], gap_right))
        gaps = []
        gap_counts = dict()

        # append chunks between meetings
        for i in range(len(endTime)):
            if i + 1 >= len(startTime):
                break
            gaps.append(gap_left)
            gap_counts[gap_left] = gap_counts.get(gap_left, 0) + 1
            gap_left = startTime[i + 1] - endTime[i]
            gap_right = startTime[i + 2] - endTime[i + 1] if i + 2 < len(startTime) else eventTime - endTime[i + 1]
            chunks.append((gap_left, endTime[i + 1] - startTime[i + 1], gap_right))
        
        gaps.append(gap_left)
        gap_counts[gap_left] = gap_counts.get(gap_left, 0) + 1
        gaps.append(gap_right)
        gap_counts[gap_right] = gap_counts.get(gap_right, 0) + 1

        gaps.sort()

        largest_free_time = 0
        for left, duration, right in chunks:
            # find available gap that can fit the meeting
            index = bisect.bisect_left(gaps, duration)
            # no gaps large enough to fit the meeting
            if index >= len(gaps):
                largest_free_time = max(largest_free_time, left + right)
                continue

            gap_size = gaps[index]
            similar_count = 0
            if gap_size == left:
                similar_count += 1
            if gap_size == right:
                similar_count += 1

            if gap_counts[gap_size] > similar_count:
                largest_free_time = max(largest_free_time, left + duration + right)
                continue
            # equal
            is_found = False
            for i in range(index + 1, len(gaps)):
                if gaps[i] != left and gaps[i] != right:
                    is_found = True
                    break

            if is_found:
                largest_free_time = max(largest_free_time, left + duration + right)
            else:
                largest_free_time = max(largest_free_time, left + right)
            
        return largest_free_time
        