class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            lookup=target-nums[i]
            if lookup in hash:
                j=hash[lookup]
                if i<j:
                    return [i,j]
                else:
                    return [j,i]
            else:
                hash[nums[i]]=i