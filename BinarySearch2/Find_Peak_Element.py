#TimeComplexity: O(log n)
#SpaceComplexity: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: # if nums array is empty
            return -1
        l = 0 #assigning to left pointer
        h = len(nums) - 1 #assigning to right pointer
        
        while l<=h: # until low is lesser than high
            mid = l + (h-l) // 2 # finding mid value
            if (mid == 0 or nums[mid]>nums[mid-1]) and (mid == len(nums) -1 or nums[mid]>nums[mid+1]): # if (mid is first or mid is greater than mid-1) and (mid is last or mid is greater than mid+1)
                return mid 
            elif mid>0 and nums[mid] < nums[mid-1]: # if mid is lesser than mid-1 and mid is greater than 0
                h=mid-1 # move high to mid-1
            else:
                l=mid+1 # move low to mid+1
        return -1
