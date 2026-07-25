class Solution(object):
    def searchRange(self, nums, target):

        def find_first():
            lower = 0
            upper = len(nums) - 1
            answer = -1

            while lower <= upper:
                mid = lower + (upper - lower) // 2

                if nums[mid] == target:
                    answer = mid
                    upper = mid - 1

                elif nums[mid] < target:
                    lower = mid + 1

                else:
                    upper = mid - 1

            return answer

        def find_last():
            lower = 0
            upper = len(nums) - 1
            answer = -1

            while lower <= upper:
                mid = lower + (upper - lower) // 2

                if nums[mid] == target:
                    answer = mid
                    lower = mid + 1

                elif nums[mid] < target:
                    lower = mid + 1

                else:
                    upper = mid - 1

            return answer

        return [find_first(), find_last()]