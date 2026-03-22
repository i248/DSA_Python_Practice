# Example 1:
# Input:N = 153
# Output:True
# Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153

class Solution:
    def isArmstrong(self, n):
        sum = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        return sum == n
N = 153
obj = Solution()
print("Is Given Number is Armstrong Number :", obj.isArmstrong(N))

