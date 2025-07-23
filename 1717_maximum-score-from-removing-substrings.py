# https://leetcode.com/problems/maximum-score-from-removing-substrings/

def maximumGain(s, x, y):
    """
    :type s: str
    :type x: int
    :type y: int
    :rtype: int
    """
    substrings = dict()
    substrings['ab'] = x
    substrings['ba'] = y
    string_to_search_first = 'ab' if x >= y else 'ba'
    string_to_search_second = 'ba' if x >= y else 'ab'

    first_stack = []
    total_points = 0
    for character in s:
        first_stack.append(character)
        if len(first_stack) < 2:
            continue
        if ''.join(first_stack[-2:]) != string_to_search_first:
            continue
        del first_stack[-2:]
        total_points += substrings[string_to_search_first]
        
    second_stack = []
    for character in first_stack:
        second_stack.append(character)
        if len(second_stack) < 2:
            continue
        if ''.join(second_stack[-2:]) != string_to_search_second:
            continue

        del second_stack[-2:]
        total_points += substrings[string_to_search_second]
        
    return total_points

s = "cdbcbbaaabab"
x = 4
y = 5

print(maximumGain(s, x, y))  # Output: 19
        