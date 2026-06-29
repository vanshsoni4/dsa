class Solution(object):
    def maxSubArray(self, nums):
        currntsum = 0
        maxsum = nums[0]
        for num in nums:
            if currntsum < 0:
                currntsum = 0
            currntsum += num
            maxsum = max(maxsum,currntsum)
        return maxsum

