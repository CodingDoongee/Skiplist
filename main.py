class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def __call__(self, *args, **kwargs):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.tail = 0
        self.tailnode = None
        self.startnode = None
        self.__tempnode = None

    def Append(self, node):
        if self.tailnode is not None:
            self.tailnode.next = node
            self.tailnode = node
            self.tail += 1
        else:
            self.startnode = node
            self.tailnode = node
            self.tail = 1

    def AddNode(self, indx, node):
        if indx == 0:
            self.startnode = node
            self.tailnode = node
            self.tail = self.tail + 1
        elif indx >= self.tail:
            self.tailnode.next = node
            self.tail = self.tail + 1
            self.tailnode = node
        else:
            self.__tempnode = self.startnode
            for _ in range(indx-1):
                self.__tempnode = self.__tempnode.next
            node.next = self.__tempnode.next
            self.__tempnode.next = node
            self.tail += 1

    def RemoveNode(self, target):
        self.__tempnode = self.startnode
        if self.__tempnode.data == target:
            self.startnode = self.__tempnode.next
            self.tail -= 1
        elif self.tailnode.data == target:
            for _ in range(self.tail-1):
                self.__tempnode = self.__tempnode.next
            self.tailnode = self.__tempnode
            self.tail -= 1
        else:
            for _ in range(self.tail):
                if self.__tempnode.next.data == target:
                    self.__tempnode.next = self.__tempnode.next.next
                    self.tail -= 1
                    break
                else:
                    self.__tempnode = self.__tempnode.next

    def SearchNode(self, target):
        self.__tempnode = self.startnode
        for indx in range(self.tail):
            if self.__tempnode.data == target:
                return indx
            else:
                self.__tempnode = self.__tempnode.next
        return None

    def Clear(self):
        self.startnode = None
        self.tailnode = None
        self.__tempnode = None
        self.tail = 0

    def __call__(self, *args, **kwargs):
        self.__tempnode = self.startnode
        for i in range(self.tail):
            print(self.__tempnode.data)
            self.__tempnode = self.__tempnode.next


# class Skiplist(object):
#     MaxLavel = 0
#
#     def __init__(self):
#         self.LinkedList = LinkedList()
#
#     def search(self, target):
#         """
#         :type target: int
#         :rtype: bool
#         """
#         self.LinkedList = self.LinkedList
#         for i in range(len(self.LinkedList)):
#             if target == Node.data:
#                 return True
#             else:
#                 Node = Node.next
#         return False
#
#
#     def add(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#
#     def erase(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
#
# obj = Skiplist()
# param_1 = obj.search(4)
