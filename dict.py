# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()      # Dummy node to start the result list
        current = dummy
        carry = 0               # Carry starts at 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0   # Get current value of l1
            val2 = l2.val if l2 else 0   # Get current value of l2

            total = val1 + val2 + carry
            carry = total // 10          # Update carry
            current.next = ListNode(total % 10)  # Create new node for the digit
            current = current.next       # Move to next in result

            # Move to the next nodes in input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the real head (skip dummy)

def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end=' -> ' if node.next else '\n')
        node = node.next

# Example
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Should print: 7 -> 0 -> 8
