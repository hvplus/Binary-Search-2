""" Time Complexity : O(logn)
 Space Complexity : O(1)
 Did this code successfully run on Leetcode :Yes
 Any problem you faced while coding this : No """

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low,high = 0,len(nums) - 1
        
        while low <= high:
            
            mid = int(low + (high-low)/2)
            if nums[low] < nums[high]:
                return nums[low]
            
            elif (mid == 0 or nums[mid] < nums [mid-1]) and \
                (mid == len(nums)-1 or nums[mid] < nums[mid+1]):
                return nums[mid]
            
            elif(nums[mid] < nums[low]):
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
            
            
        