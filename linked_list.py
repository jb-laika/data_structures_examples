class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

    def __str__(self):
        return "<" + str(self.data) + ">"


# ------------------------------------
class LinkedList:

    def __init__(self):
        self.head = None  # always points to first node in list
        self.num_nodes = 0  # counter keeps track of number of nodes in list
        self.last = None  # always points to last node in list

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        if self.size() == 0:
            self.head = temp
            self.last = temp
        else:
            self.head.setPrev(temp)
            temp.setNext(self.head)
            self.head = temp
        self.num_nodes += 1

    def pop(self):
        return self.remove(self.size() - 1)

    def get(self, index):
        final = self.head
        for i in range(self.size()):
            if i == index:
                return final
            final = final.next
        raise IndexError("Index is out of range for the linked list.")

    def index(self, item):
        final = self.head
        for i in range(self.size()):
            if final.data == item:
                return i
            final = final.next
        raise ValueError("Item not found in linked list.")

    def insert(self, index, item):
        temp = Node(item)
        final = self.head
        if self.size() == 0 or index == 0:
            self.add(item)
            return None
        elif index >= self.size():
            self.append(item)
            return None
        elif index < 0:
            raise IndexError("Index is out of range for the linked list.")
        elif self.size() > 0:
            for i in range(self.size()):
                if i == index:
                    temp.setNext(final)
                    temp.setPrev(final.getPrev())
                    final.prev.setNext(temp)
                    final.setPrev(temp)
                    self.num_nodes += 1
                    return None
                final = final.getNext()

    def load(self, data):
        """convenience function to bulk-add items from a Python iterable like a list or range result"""
        for i in data:
            self.add(i)

    def size(self):
        return self.num_nodes

    def append(self, item):
        temp = Node(item)
        if self.size() == 0:
            self.last = temp
            self.head = temp
        elif self.size() == 1:
            temp.setPrev(self.last)
            self.last = temp
            self.head.setNext(self.last)
        else:
            self.last.setNext(temp)
            temp.setPrev(self.last)
            self.last = temp
        self.num_nodes += 1
        return None

    def remove(self, index):
        current = self.head
        if index < 0 or index >= self.size():
            raise IndexError("Index is out of range for the linked list.")
        elif self.size() == 1:
            store_data = self.head.data
            self.head = None
            self.last = None
            self.num_nodes -= 1
            return store_data
        elif index == 0:
            store_data = self.head.data
            self.head = current.next
            self.num_nodes -= 1
            return store_data
        elif index == self.size() - 1:
            store_data = self.last.data
            self.last = self.last.getPrev()
            self.last.setNext(None)
            self.num_nodes -= 1
            return store_data
        else:
            for i in range(self.size()):
                if i == index:
                    current.prev.setNext(current.getNext())
                    self.num_nodes -= 1
                    return current.getData()
                current = current.getNext()

    def __str__(self):
        res = "["
        current = self.head
        while current is not None:
            res += str(current) + ","
            current = current.getNext()
        return res + "]"

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found


# ------------------------------------
def test_add():
    list1 = LinkedList()
    list1.add(7)
    assert list1.head.data == 7, 'after add(7), head has data value ' + str(list1.head.data) + ' not 7'
    assert list1.size() == 1, 'size() does not return 1 after adding item to empty list'

    list1.add(3)
    assert list1.head.data == 3, 'after add(3), head has data value ' + str(list1.head.data) + ' not 3'
    assert list1.size() == 2, 'size() does not return 2 after adding 2nd item to empty list'


# ------------------------------------
def test_size():
    list1 = LinkedList()
    assert list1.size() == 0, 'size() fails on an empty list'
    list1.add(7)
    assert list1.size() == 1, 'size() fails after adding item to empty list'

    list2 = LinkedList()
    list2.load([3, 1, 4, 2])
    assert list2.size() == 4, 'size() fails after using load() to put 4 items into empty list'


# ------------------------------------
def test_append():
    list1 = LinkedList()
    list1.append(7)
    assert list1.head.data == 7, 'after add(7), head has data value ' + str(list1.head.data) + ' not 7'
    assert list1.size() == 1, 'size() does not return 1 after appending item to empty list'

    list1.append(3)
    assert list1.last.data == 3, 'after append(3), last has data value ' + str(list1.last.data) + ' not 3'
    assert list1.size() == 2, 'size() does not return 2 after adding 2nd item to empty list'


# ------------------------------------
def test_pop():
    list1 = LinkedList()
    list1.add(7)
    list1.append(3)
    list1.append(6)
    list1.append(1)
    assert list1.pop() == 1, 'pop() returns data value ' + str(list1.pop()) + ' not 1'

    list2 = LinkedList()
    list2.add(7)
    list2.append(3)
    list2.pop()
    assert list2.last.data == 7, 'after pop(), last has data value ' + str(list2.last.data) + ' not 7'

    list3 = LinkedList()
    list3.add(7)
    list3.pop()
    assert list3.last is None, 'after pop(), last has data value ' + str(list3.last.data) + ' not None'
    assert list3.head is None, 'after pop(), head has data value ' + str(list3.head.data) + ' not None'


# ------------------------------------
def test_get():
    list1 = LinkedList()
    list1.add(7)
    list1.append(3)
    list1.append(6)
    assert list1.get(1).data == 3, 'get() returns data value ' + list1.get(1).data + ' not 3'


# ------------------------------------
def test_index():
    list1 = LinkedList()
    list1.add(7)
    list1.append(3)
    list1.append(6)
    assert list1.index(7) == 0, 'index() returns position ' + list1.index(7) + ' not 1'
    assert list1.index(3) == 1, 'index() returns position ' + list1.index(3) + ' not 1'
    assert list1.index(6) == 2, 'index() returns position ' + list1.index(6) + ' not 1'


# ------------------------------------
def test_insert():
    list1 = LinkedList()
    list1.add(7)
    list1.append(3)
    list1.append(6)
    list1.append(2)
    list1.append(5)
    list1.insert(2, 8)
    assert list1.get(2).data == 8, 'after insert(2, 8), get(2) points to ' + str(list1.get(2).data) + ' not 8'

    list2 = LinkedList()
    list2.insert(2, 1)
    assert list2.head.next is None, 'after insert(2, 1), head points to ' + str(list2.head.next) + ' not None'


# ------------------------------------
def test_remove():
    list1 = LinkedList()
    list1.add(7)
    list1.append(3)
    list1.append(6)
    list1.append(2)
    assert list1.head.data == 7, 'after remove(1), head points to ' + str(list1.head.data) + ' not 7'
    assert list1.last.data == 2, 'after remove(1), last points to ' + str(list1.last.data) + ' not 2'

    list2 = LinkedList()
    list2.add(7)
    list2.remove(0)
    assert list2.head is None, 'after remove(0), head points to ' + str(list2.head) + ' not None'
    assert list2.last is None, 'after remove(0), last points to ' + str(list2.last) + ' not None'


if __name__ == "__main__":
    test_size()
    test_add()
    test_append()
    test_pop()
    test_get()
    test_index()
    test_insert()
    test_remove()

