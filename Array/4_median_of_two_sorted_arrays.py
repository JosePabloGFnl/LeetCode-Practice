class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine both arrays
        nums = nums1 + nums2
        # Sort
        nums.sort()
        # Return median
        tmp = sorted(nums)
        mid = len(tmp) // 2
        return (tmp[mid] + tmp[-mid-1]) / 2
