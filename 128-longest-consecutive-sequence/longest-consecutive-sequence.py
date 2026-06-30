class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0
        for num in numset:
            if num-1 not in numset:
                current = num
                length = 1
                while current + 1 in numset:
                    current += 1
                    length +=1
                longest = max(longest,length)
        return longest

              
        """
        :type nums: List[int]
        :rtype: int
        """
        