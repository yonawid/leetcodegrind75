# Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # the number stored in this node
        self.next = next    # pointer to the next node

class Solution:

    # ITERATIVE APPROACH
    # Time:  O(n + m) — visit every node in both lists once
    # Space: O(1)     — only two extra pointers, no new nodes created
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Dummy node gives us a stable starting point (avoids edge cases on head)
        dummynode = ListNode()
        curpos = dummynode   # curpos builds the merged list step by step

        while list1 and list2:
            if list1.val > list2.val:
                # list2's node is smaller — attach it next
                curpos.next = list2
                list2 = list2.next       # advance list2
                curpos = curpos.next     # advance builder pointer
            else:
                # list1's node is smaller or equal — attach it next
                curpos.next = list1
                list1 = list1.next       # advance list1
                curpos = curpos.next     # advance builder pointer

        # One list is exhausted — attach the remainder of the other directly
        curpos.next = list1 or list2

        # dummy.next is the real head of the merged list (skip the dummy)
        return dummynode.next


    # RECURSIVE APPROACH
    # Time:  O(n + m) — each node is processed exactly once
    # Space: O(n + m) — call stack grows with each recursive call
    def mergeTwoLists2(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Base cases: if either list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            # list1's node leads — recursively merge the rest
            list1.next = self.mergeTwoLists2(list1.next, list2)
            return list1   # return list1 as the head of this merged segment
        else:
            # list2's node leads — recursively merge the rest
            list2.next = self.mergeTwoLists2(list1, list2.next)
            return list2   # return list2 as the head of this merged segment