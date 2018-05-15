class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return list(set(nums))

if __name__ == "__main__":
    nums = [1, 1, 2]
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    new_list = Solution().removeDuplicates(nums1)

    print(new_list)