class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        count = 0
        if nums_length == 0:
            return 0
        for i in range(nums_length):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        count += 1
        return count

    def bestRemoveDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(set(nums))
                        
        

if __name__ == "__main__":
    nums = [1, 1, 2]
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    new_list = Solution().removeDuplicates(nums)

    print(new_list)