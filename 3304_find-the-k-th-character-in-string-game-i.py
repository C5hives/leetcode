# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        return self.helper(k)
        
    def helper(self, k):
        if k == 1:
            return "a"
        
        # calculate previous index needed to compute current k value
        previous_power_of_two = math.pow(2, math.ceil(math.log(k) / math.log(2)) - 1)
        previous_k = k - previous_power_of_two
        
        character_at_k = chr(ord(self.helper(previous_k)) + 1)
        return character_at_k