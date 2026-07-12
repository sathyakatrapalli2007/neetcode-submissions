class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(len(nums)*2)
        n=len(nums)
        for i in range(len(nums)*2):
            if i<n:
                ans[i]=nums[i]
            else:
                i=i%len(nums)
                ans[n+i]=nums[i]
        return ans
        