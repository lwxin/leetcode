class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        int_num = 0
        roman_str = ''
        for i in s:
            int_num += romanDict[i]
            roman_str += i
            if len(roman_str) >= 2 and roman_str[-2:] in romanDict:
                int_num -= romanDict[roman_str[-2]] * 2
        return int_num

    def bestRomanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        hmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = hmap[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if hmap[s[i]] < hmap[s[i+1]]:
                ans -= hmap[s[i]]
            else:
                ans += hmap[s[i]]
        return ans

if __name__ == '__main__':
	test_list = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
	for i in test_list:
		num = Solution()
		print(num.romanToInt(i))
