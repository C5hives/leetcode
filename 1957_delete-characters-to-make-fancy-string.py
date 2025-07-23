# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_character = ''
        count = 0
        final_string = ''
        for character in s:
            if last_character == '':
                last_character = character
                count += 1
                final_string += character
                continue
            
            if character != last_character:
                last_character = character
                count = 1
                final_string += character
                continue
            
            if count == 2:
                continue
            
            final_string += character
            count += 1
        
        return final_string