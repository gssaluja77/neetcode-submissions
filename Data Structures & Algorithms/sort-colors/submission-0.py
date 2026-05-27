class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = Counter()
        
        for num in nums:
            counts[num] += 1
        
        i = 0
        for j in range(0, 3):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1
            
        return nums