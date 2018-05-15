class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            num_to_sum = target - nums[i]
            if num_to_sum in nums[(i + 1):]:
                return [i, (nums[(i+1):].index(num_to_sum)) + i + 1]


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    test_algorithem = Solution()
    print(test_algorithem.twoSum(nums, target))