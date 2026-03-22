# Input: N = 36
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
# Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

class Solution:
    def getDivisors(self , n):
        divisor = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisor.append(i)
        return divisor
N = 36
obj =  Solution()
print("Divisor of Given Number is :", obj.getDivisors(N))