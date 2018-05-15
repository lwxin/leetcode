class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
        else:
            reverse_num = 0
            flag = True
            numerator = x      # 121
            while flag:
                remainder = numerator % 10  # 1  2   1
                reverse_num = reverse_num * 10 + remainder
                numerator //= 10            # 12   1  0
                if numerator <= 0:
                    flag = False
            if reverse_num == x:
                return True
            else:
                return False

if __name__ == '__main__': 
    test_list = [121, -121, 10]
    for i in test_list:
        print(Solution().isPalindrome(i))    