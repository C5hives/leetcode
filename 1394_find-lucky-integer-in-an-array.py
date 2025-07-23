# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        frequencies = dict()
        for number in arr:
            if number not in frequencies:
                frequencies[number] = 0
            frequencies[number] += 1
        
        largest_lucky_number = -1
        for number, frequency in frequencies.items():
            if number != frequency:
                continue
            
            if number < largest_lucky_number:
                continue
            largest_lucky_number = number
        
        return largest_lucky_number