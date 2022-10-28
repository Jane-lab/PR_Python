from re import I

class Solution:
    def MultipleOf3And5(self, num: int) -> int:
        sum = 0
        for i in range(1, num):
            if(i%3==0 or i%5==0):
                sum = sum + i
        return sum
num = 1000
so = Solution()
print(Solution().MultipleOf3And5(num))
