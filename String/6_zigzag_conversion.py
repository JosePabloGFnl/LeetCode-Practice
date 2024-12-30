"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        sub_strings = {f'sub_s{i}': '' for i in range(1, numRows + 1)}
        i = 1
        zigzag = 1
        
        for c in s:
            sub_strings[f'sub_s{i}'] = sub_strings[f'sub_s{i}'] + c
            
            if zigzag == 1 and i == numRows:
                zigzag = -1
            elif zigzag == -1 and i == 1:
                zigzag = 1
                
            i += zigzag
                
        result = ''.join(sub_strings[f'sub_s{i}'] for i in range(1, numRows + 1))
        return result
