# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

import math

class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        return self.helper(k, operations)
    
    def helper(self, k, operations):
        if k == 1:
            return "a"
        
        # calculate number of times word needs to be doubled for its length to be >= k
        number_of_operations = int(math.ceil(math.log(k) / math.log(2)) - 1)
        # calculate previous index needed to compute current k value
        previous_power_of_two = math.pow(2, number_of_operations)
        previous_k = k - previous_power_of_two

        if operations[number_of_operations] == 0: # append only
            return self.helper(previous_k, operations)
        else: # increment then append
            return self.next_character(self.helper(previous_k, operations))
    
    def next_character(self, character):
        if character == "z":
            return "a"
        return chr(ord(character) + 1)