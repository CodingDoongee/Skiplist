import random


class Node:
    def __init__(self, data, level=0):
        self.data = data
        self.next = None
        self.before = None
        self.down = None
        self.up = None
        self.level = level

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
            node.before = self.tailnode
            self.tailnode.next = node
            self.tailnode = node
            self.tail += 1
        else:
            self.startnode = node
            self.tailnode = node
            self.tail = 1

    def AddNodeValue(self, node):
        self.__tempnode = self.startnode
        if self.tail == 0:
            self.startnode = node
            self.tailnode = self.startnode
            self.tail = 1
        else:
            for _ in range(self.tail):
                if self.__tempnode.next is None:
                    if self.__tempnode.data < node.data:
                        self.__tempnode.next = node
                        self.tailnode = node
                        node.next = None
                        node.before = self.__tempnode
                        self.tail += 1
                    else:
                        if self.__tempnode.before is not None:
                            self.__tempnode.before.next = node
                            node.before = self.__tempnode.before
                        else:
                            self.startnode = node
                            node.before = None
                        node.next = self.__tempnode
                        self.__tempnode.before = node
                        self.tail += 1
                elif self.__tempnode.data == self.startnode.data and node.data < self.__tempnode.data:
                    node.next = self.startnode
                    node.before = None
                    self.startnode = node
                    self.tail += 1

                elif self.__tempnode.data < node.data <= self.__tempnode.next.data:
                    node.next = self.__tempnode.next
                    self.__tempnode.next = node.data
                    node.before = self.__tempnode
                    self.tail += 1
                else:
                    self.__tempnode = self.__tempnode.next

    def AddNodeIndx(self, indx, node):
        if indx == 0:
            node.next = self.startnode
            node.before = None
            self.startnode = node
            self.tail = self.tail + 1
        elif indx >= self.tail:
            node.before = self.tailnode
            self.tailnode.next = node
            self.tail = self.tail + 1
            self.tailnode = node
        else:
            self.__tempnode = self.startnode
            for _ in range(indx - 1):
                self.__tempnode = self.__tempnode.next
            node.next = self.__tempnode.next
            self.__tempnode.next = node
            node.before = self.__tempnode
            node.next.before = node
            self.tail += 1

    def RemoveNode(self, target):
        self.__tempnode = self.startnode
        if self.startnode.data == target.data:
            self.startnode = self.__tempnode.next
            self.__tempnode.before = None
            if self.startnode is not None:
                self.startnode.before = None
            self.tail -= 1
            if self.tail == 0:
                self.tailnode = None
        elif self.tailnode.data == target.data:
            for _ in range(self.tail - 2):
                self.__tempnode = self.__tempnode.next
            self.__tempnode.next = None
            self.tailnode = self.__tempnode
            self.tail -= 1
        else:
            for _ in range(self.tail):
                if self.__tempnode.next.data == target.data:
                    self.__tempnode.next = self.__tempnode.next.next
                    self.__tempnode.next.before = self.__tempnode
                    self.tail -= 1
                    break
                else:
                    self.__tempnode = self.__tempnode.next

    def SearchNode(self, target):
        self.__tempnode = self.startnode
        for indx in range(self.tail):
            if self.__tempnode.data == target.data:
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


class Skiplist(object):
    def __init__(self):
        self.level = 0
        self.LinkedLists = list()
        self.LinkedLists.append(LinkedList())

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        TgtNode = self.LinkedLists[self.level].startnode
        if TgtNode is None:
            return False
        else:
            while TgtNode is not None:
                if target == TgtNode.data:
                    return True
                elif target < TgtNode.data:
                    if TgtNode.down is not None:
                        TgtNode = TgtNode.down
                        if TgtNode.before is not None:
                            if target > TgtNode.before.data:
                                pass
                            elif target == TgtNode.before.data:
                                return True
                            else:
                                TgtNode = TgtNode.before
                        else:
                            pass
                    else:
                        return False
                else:
                    if TgtNode.next is not None:
                        TgtNode = TgtNode.next
                    else:
                        TgtNode = TgtNode.down
            return False

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """

        def CoinTossGeneration(self2, target_node):
            if random.random() > 0.01:
                add_node2 = Node(target_node.data, target_node.level+1)
                add_node2.down = target_node
                target_node.up = add_node2
                if add_node2.level > self2.level:
                    self2.level += 1
                    self2.LinkedLists.append(LinkedList())
                self2.LinkedLists[add_node2.level].AddNodeValue(add_node2)
                CoinTossGeneration(self2, add_node2)
            else:
                pass

        TgtNode = self.LinkedLists[self.level].startnode
        if TgtNode is None:
            self.LinkedLists[self.level].startnode = Node(num, self.level)
            self.LinkedLists[self.level].tailnode = self.LinkedLists[self.level].startnode
            self.LinkedLists[self.level].tail = 1
        else:
            while TgtNode is not None:
                if num <= TgtNode.data:
                    if TgtNode.down is None:
                        if num == TgtNode.data:
                            CoinTossGeneration(self, TgtNode)
                            break
                        else:
                            if num > TgtNode.before.data:
                                add_node = Node(num, 0)
                                add_node.down = None
                                add_node.level = 0
                                self.LinkedLists[0].AddNodeIndx(self.LinkedLists[0].SearchNode(TgtNode), add_node)
                                CoinTossGeneration(self, add_node)
                                break
                            else:
                                TgtNode = TgtNode.before
                    else:
                        TgtNode = TgtNode.down
                else:
                    if TgtNode.next is None:
                        if TgtNode.down is None:
                            add_node = Node(num, 0)
                            add_node.down = None
                            add_node.level = 0
                            self.LinkedLists[0].Append(add_node)
                            CoinTossGeneration(self, add_node)
                            break
                        else:
                            TgtNode = TgtNode.down
                    else:
                        TgtNode = TgtNode.next

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        TgtNode = self.LinkedLists[0].startnode
        for _ in range(self.LinkedLists[0].SearchNode(Node(num, self.level))):
            TgtNode = TgtNode.next

        while TgtNode is not None:
            UpNode = TgtNode.up
            self.LinkedLists[TgtNode.level].RemoveNode(TgtNode)
            TgtNode = UpNode
        return True

# Your Skiplist object will be instantiated and called as such:
obj = Skiplist()
obj.add(0)
obj.add(5)
obj.add(2)
obj.add(1)
print(obj.search(0))
obj.erase(5)
print(obj.search(2))
print(obj.search(3))
print(obj.search(2))