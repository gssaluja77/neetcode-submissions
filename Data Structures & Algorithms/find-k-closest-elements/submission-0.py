class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - 1

        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            elif abs(arr[l] - x) < abs(arr[r] - x):
                r -= 1
            else:
                if arr[l] <= arr[r]:
                    r -= 1
                else:
                    l += 1
        return arr[l:r+1]