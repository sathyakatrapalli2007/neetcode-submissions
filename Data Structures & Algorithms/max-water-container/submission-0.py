class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start=0
        end = len(heights)-1
        max=0
        while start<end:
            new_max=min(heights[start],heights[end])*(end-start)
            if new_max>max:
                max=new_max
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        return max
