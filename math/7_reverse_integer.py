"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""
class Solution:
    def reverse(self, x: int) -> int:

        result = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)

        MIN_32BIT = -2**31
        MAX_32BIT = 2**31 - 1
        if MIN_32BIT <= result <= MAX_32BIT:
            result = result
        else:
            result = 0
            
        return result
        
