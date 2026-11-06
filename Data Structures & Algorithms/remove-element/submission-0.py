class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        start=0
        while start<len(nums):
            if nums[start]!=val:
                nums[i]=nums[start]
                start+=1  
                i+=1  
            else:
                while start<len(nums) and nums[start]==val:
                    start+=1
        return i
            