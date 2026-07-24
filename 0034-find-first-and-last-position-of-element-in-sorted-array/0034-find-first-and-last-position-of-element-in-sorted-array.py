class Solution(object):
    def binarysearchleft(self,nums,target):
        n =len(nums)
        low,high =0,n-1
        index=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                index=mid
                high = mid-1
            elif nums[mid]>target:
                high =  mid-1
            else:
                low=mid+1
        return index
    def binarysearchright(self,nums,target):
        n = len(nums)
        low,high=0,n-1
        index=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                index=mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low =mid+1
        return index
    def searchRange(self, nums, target):
        extleft = self.binarysearchleft(nums,target)
        if extleft==-1:
            return [-1,-1]
        extright = self.binarysearchright(nums,target)
        return[extleft,extright]
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        