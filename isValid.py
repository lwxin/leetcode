class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        flag = True
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
                    break
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    flag = False
                    break

        if stack:
            return False
        return flag

    def bestIsValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["{", "(", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                currBracket = stack[-1] + c
                if currBracket not in ["{}", "[]", "()"]:
                    return False
                stack.pop()
        return len(stack) == 0

# from collections import deque
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         deq = deque()
#         pair = {'(': ')', '[': ']', '{': '}'}
#         for letter in s:
#             if letter == '(' or letter == '[' or letter == '{':
#                 deq.append(letter)
#             else:
#                 if len(deq) > 0 and letter == pair[deq[-1]]:
#                     deq.pop()
#                 else:
#                     return False
        
#         return len(deq) == 0

if __name__ == '__main__':
    test_str_list = ['()', '()[]{}', '(}', '([)]', '{[]}'] 
    test_func = Solution()
    for i in test_str_list:
        print(test_func.isValid(i))