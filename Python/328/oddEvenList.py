class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def VectorToLinkedList(vec):
    result = ListNode(None)
    curr = result
    for i in vec:
        curr.next = ListNode(i)
        curr = curr.next
    return result.next



class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddhead = odd = head
        if head:
            evenhead = even = head.next
        while head and odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        if head:
            odd.next = evenhead
        return oddhead


list = VectorToLinkedList([12, 3, 43, 4, 34, 2, 4, 3])
test = Solution()
test.oddEvenList(list)

