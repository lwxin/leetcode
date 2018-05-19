class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 1:
            i = strs[0]
            flag = 0 
            while len(i) > 0:
                for j in strs[1:]:
                    if i == j[:len(i)]:
                        flag += 1
                        if flag == len(strs) - 1:
                            return i
                    else:
                        i = i[:-1]
                        flag = 0
                    
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            return ''

if __name__ == '__main__': 
    test_list = [['c', 'acc', 'ccc'], ['a'], ['flower', 'flow', 'flight'], ['dog', 'reavecar', 'car']]
    for i in test_list:
        prefix = Solution()
        print(prefix.longestCommonPrefix(i), '------')
