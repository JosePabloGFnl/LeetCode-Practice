"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s:
            return ""

        longest = ""

        for i in range(len(s)):
            even = expand_from_center(s, i, i + 1)
            odd = expand_from_center(s, i, i)
            
            cur_longest = even if len(even) > len(odd) else odd
            longest = cur_longest if len(cur_longest) > len(longest) else longest
            
        return longest if longest else s[0]
