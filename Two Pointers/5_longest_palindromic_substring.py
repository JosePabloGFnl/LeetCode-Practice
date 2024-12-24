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
