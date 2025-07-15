# https://leetcode.com/problems/valid-word/

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3 or not word.isalnum():
            return False
        word = word.lower()
        has_vowel = False
        has_cosonant = False
        for character in word:
            if has_vowel and has_cosonant:
                return True
            if character.isnumeric():
                continue
            if (character == 'a' or character == 'e' or
                character == 'i' or character == 'o' or character == 'u'):
                has_vowel = True
            else:
                has_cosonant = True
        return has_vowel and has_cosonant
            
