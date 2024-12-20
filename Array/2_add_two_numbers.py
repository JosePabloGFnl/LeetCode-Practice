'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Function to reverse the linked list 
        def reverse_list(head):
            new_head = None
            while head:
                head.next, head, new_head = new_head, head.next, head
            return new_head

        # Function to convert linked list to int    
        def linked_list_to_int(head: ListNode) -> int:
            num_str = ''
            current = head
            while current is not None:
                num_str += str(current.val)
                current = current.next
            return int(num_str)

        # Function to convert int to linked list
        def int_to_linked_list(number: int) -> ListNode:
            dummy_head = ListNode(0)
            current = dummy_head
            for digit in str(number):
                current.next = ListNode(int(digit))
                current = current.next
            return dummy_head.next

        # reverse lists
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        # convert lists into single int number
        l1 = linked_list_to_int(l1)
        l2 = linked_list_to_int(l2)

        # sum both lists
        answer = l1 + l2

        # convert into array
        answer = int_to_linked_list(answer)

        # reverse once again
        answer = reverse_list(answer)

        return answer
