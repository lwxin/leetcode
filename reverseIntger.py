class Solution:

    def bestReverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = -1 * int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])  
            
        if y > 2**31 or y < -2**31:
            y = 0
        return y

    def betterReverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        elif x >= 10:
            result_num = int(''.join(list(str(x))[::-1]))
            if -2**31 <= result_num <= 2**31 -1:
                return result_num
            else:
                return 0
        elif x <= -10:
            result_num = -int(''.join(list(str(abs(x)))[::-1]))
            if -2**31 <= result_num <= 2**31 -1:
                return result_num
            else:
                return 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        Without turn into list or str
        """    	
        reverse_num = 0
        flag = True
        numerator = abs(x)      
        while flag:
            remainder = numerator % 10  
            reverse_num = reverse_num * 10 + remainder
            numerator //= 10            
            if numerator <= 0:
                flag = False
        if x < 0:
            reverse_num = -reverse_num
        if -2**31 <= reverse_num <= 2**31 -1:
            return reverse_num
        else:
            return 0

if __name__ == '__main__':
    test_integer_list = [123, -123, 120]
    for i in test_integer_list:
        reversed_integer = Solution().better_reverse(i)
        print(reversed_integer)