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
    def expand_from_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:

    if len(s) % 2 == 0:
        expand_from_center(s, i, i + 1)
    else:
        expand_from_center(s, i, i)
