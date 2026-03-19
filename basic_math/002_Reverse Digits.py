# Reverse Digits of A Number
# Problem Statement: Given an integer N return the reverse of the given number.
# Input: N = 12345
# Output:54321
# Explanation: The reverse of 12345 is 54321.

# Input: N = 7789                
# Output: 9877
# Explanation: The reverse of number 7789 is 9877.

class Solution:
    def reverseDigit(self, n):
        revNum = 0
        while n > 0:
            lastDigit = n % 10
            revNum = revNum * 10 + lastDigit
            n = n // 10

        return revNum
N = 12345
obj = Solution()
print("Reverse Number of Given is :", obj.reverseDigit(N))