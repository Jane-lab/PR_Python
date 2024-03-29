#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

class Solution:
    def EvenFibonacciNumbers(self, num:int) -> int:
        
        listNum = [1,2]
        sum = 2
        while listNum[-1] <= num:
            listNum.append(listNum[-1]+listNum[-2])
            if( listNum[-1]%2==0):
                sum = sum + listNum[-1]
        return sum
num = 4000000
so = Solution()
print(Solution().EvenFibonacciNumbers(num))
