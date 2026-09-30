'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # dict of number counts
        counts = {}

        # Counting frequency of each element 
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # rank and turn into array
        counts_ranked = sorted(counts, key=counts.get, reverse=True)

        # first k elements
        res = counts_ranked[: k] 
                    
        return res
    
# This code is contributed by Ryuga
