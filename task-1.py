class Solution:
    def romanToInt(self, s: str) -> int:
        roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        total = 0
        prev_value = 0
                
        for char in reversed(s):
            curr_value = roman[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        
        return total


solution = Solution()
print(solution.romanToInt("VI"))  
print(solution.romanToInt("MIX"))
print(solution.romanToInt("III"))
print(solution.romanToInt("IV"))
print(solution.romanToInt("VIII"))
print(solution.romanToInt("IX"))
print(solution.romanToInt("CDXLIII"))