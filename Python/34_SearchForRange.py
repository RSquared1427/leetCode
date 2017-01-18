class Solution(object)
    def binary_search(self, nums, target):
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if target < nums[mid]:
                end = mid
            else:
                start = mid+1
        return start
    def searchRange(self, nums, target):
	if not nums:
            return [-1, -1]
	start = self.binary_search(nums, target-0.5)
        if nums[start] != target:
            return [-1, -1]
        nums.append(0)
        end = self.binary_search(nums, target+0.5)-1
        return [start, end]

sample = Solution()
nums = []
target = 0
sample.searchRange(nums, target)




