class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if((nums[i]+nums[j])==target):
                    return [i,j]
S=Solution()
print(S.twoSum([2,7,11,15],9))
