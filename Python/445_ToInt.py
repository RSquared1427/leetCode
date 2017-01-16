class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.linkedListToNum(l1)
        num2 = self.linkedListToNum(l2)
        summed = num1+num2
        return self.numToLinkedList(summed)
    
    def numToLinkedList(self, num):
        dummy = ListNode(None)
        curr = dummy
        for d in str(num):
            node = ListNode(int(d))
            curr.next = node
            curr = node
        return dummy.next
     
    def linkedListToNum(self, l):
        string = ""
        cur = l
        while cur:
            string += str(cur.val)
            cur = cur.next
        return int(string)
