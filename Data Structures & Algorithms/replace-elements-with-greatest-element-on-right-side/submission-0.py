class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxNum
            maxNum = max(maxNum, temp)
        
        return arr