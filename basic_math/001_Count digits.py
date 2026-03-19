# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
                        
# Example 2:
# Input:N = 7789              
# Output: 4
# Explanation: The number 7789 has 4 digits. 

class Solution:
    def countDigits(self,n):
        count = 0
        while n > 0:
            count  = count + 1
            n = n // 10
        return count 
N = 12345
obj =  Solution()
print("Number of Count Digits is :" , obj.countDigits(N))