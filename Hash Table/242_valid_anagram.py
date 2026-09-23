'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Source - https://stackoverflow.com/a/15046263
        # Posted by K Z
        # Retrieved 2026-09-23, License - CC BY-SA 3.0
        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))

        if s_sorted == t_sorted:
            return True
        return False

'''
Less time consuming solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for i in set(s):
            if(s.count(i)!=t.count(i)):
                return False
        return True
'''
