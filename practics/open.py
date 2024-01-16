class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

class Solution:
    def isValid(self, s: str) -> bool:
        o = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        stack = []

        for c in s:
            if c in o:
                if not (
                    stack
                    and (stack.pop() == o[c])
                ):
                    return False
            else:
                stack.append(c)
        return not stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumy = ListNode(0)
        tail = dumy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dumy.next
            
