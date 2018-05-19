# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is None and l2 is None:
        #     return None
        # new_list = ListNode(0)
        # pre = new_list
        # while l1 is not None and l2 is not None:
        #     if l1.val < l2.val:
        #         pre.next = l1
        #         l1 = l1.next
        #     else:
        #         pre.next = l2
        #         l2 = l2.next
        #     pre = pre.next
        # if l1 is not None:
        #     pre.next = l1
        # else:
        #     pre.next = l2
        # return new_list.next

        # if not l1:  
        #     return l2  
        # elif not l2:  
        #     return l1  
        # else:  
        #     if l1.val <= l2.val:  
        #         l1.next = self.mergeTwoLists(l1.next, l2)  
        #         return l1  
        #     else:  
        #         l2.next = self.mergeTwoLists(l1, l2.next)  
        #         return l2
        
        # new_list = ListNode(0)
        # new_list.next = l1
        # prev, head_of_1, head_of_2 = new_list, l1, l2

        # while head_of_2:
        #     if not head_of_1:
        #         prev.next = head_of_2
        #         break
        #     if head_of_1.val > head_of_2.val:
        #         temp = head_of_2
        #         head_of_2 = head_of_2.next
        #         prev.next = temp
        #         temp.next = head_of_1
        #         prev = prev.next
        #     else:
        #         head_of_1, prev = head_of_1.next, head_of_1
        # return new_list.next

        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l3, l1 = l1, l1.next
        else:
            l3, l2 = l2, l2.next
        
        cur = l3
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return l3

if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = [1, 2, 4]
    l2 = ListNode(0)
    l2.next = [1, 1, 4]
    test_func = Solution()

    print(test_func.mergeTwoLists(l1, l2))
