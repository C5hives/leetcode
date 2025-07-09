# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_hashmap = dict()
        for index, number in enumerate(nums):
            if number not in number_hashmap:
                number_hashmap[number] = set()
            number_hashmap[number].add(index)

        for index, number in enumerate(nums):
            needed_number = target - number
            if needed_number not in number_hashmap:
                continue
            indexes = list(number_hashmap[needed_number])
            for i in indexes:
                if i == index:
                    continue
                return [i, index]
        