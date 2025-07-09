# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.counts_of_one = dict()
        self.counts_of_two = dict()
        self.nums2 = nums2

        for number in nums1:
            if number not in self.counts_of_one:
                self.counts_of_one[number] = 0
            self.counts_of_one[number] += 1
        
        for number in nums2:
            if number not in self.counts_of_two:
                self.counts_of_two[number] = 0
            self.counts_of_two[number] += 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        original_number = self.nums2[index]
        new_number = original_number + val
        self.nums2[index] = new_number

        self.counts_of_two[original_number] -= 1
        if new_number not in self.counts_of_two:
            self.counts_of_two[new_number] = 0
        self.counts_of_two[new_number] += 1
        
    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        total_pairs = 0
        for number, count in self.counts_of_one.items():
            complement = tot - number
            if complement not in self.counts_of_two:
                continue
            total_pairs += count * self.counts_of_two[complement]
        return total_pairs
        
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)