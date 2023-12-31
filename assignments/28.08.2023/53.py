class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax=nums[0]
        maxSum = nums[0]

        for i in range(1,len(nums)):
            currentMax=max(nums[i],currentMax+nums[i]);
            if currentMax > maxSum:
                maxSum = currentMax
            if currentMax <0:
                currentMax=0
        return maxSum