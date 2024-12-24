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

        longest = ""

        for i in range(len(s)):
            if len(s) % 2 == 0:
                even = expand_from_center(s, i, i + 1)
                if len(even) > len(longest):
                        longest = even
            else:
                odd = expand_from_center(s, i, i)
                if len(odd) > len(longest):
                        longest = odd
        return longest
