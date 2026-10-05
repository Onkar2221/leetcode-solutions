
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        list1_data = []

        while list1:
            list1_data.append(list1.val)
            list1 = list1.next

        list2_data = []

        while list2:
            list2_data.append(list2.val)
            list2 = list2.next

        temp = 0

        for j in range(len(list1_data) - 1):
            for index, i in enumerate(list1_data):

                if index == len(list1_data) - 1:
                    break

                if list1_data[index] > list1_data[index + 1]:

                    temp = list1_data[index]
                    list1_data[index] = list1_data[index + 1]
                    list1_data[index + 1] = temp

        print(list1_data)

        temp2 = 0

        for j in range(len(list2_data) - 1):
            for index, i in enumerate(list2_data):

                if index == len(list2_data) - 1:
                    break

                if list2_data[index] > list2_data[index + 1]:

                    temp2 = list2_data[index]
                    list2_data[index] = list2_data[index + 1]
                    list2_data[index + 1] = temp2

        print(list2_data)

        index1 = 0
        index2 = 0
        result = []

        while index1 < len(list1_data) and index2 < len(list2_data):

            if list1_data[index1] > list2_data[index2]:

                result = result + [list2_data[index2]]
                index2 = index2 + 1

            else:

                result = result + [list1_data[index1]]
                index1 = index1 + 1

        while index1 < len(list1_data):

            result = result + [list1_data[index1]]
            index1 = index1 + 1

        while index2 < len(list2_data):

            result = result + [list2_data[index2]]
            index2 = index2 + 1

        answer = ListNode()
        current = answer

        for value in result:
            current.next = ListNode(value)
            current = current.next

        return answer.next

