"""
author: Pratik Kulkarni

CSCI-605 Lab 6 Priority Queue
This class makes a priority queue which works as a FIFO queue but it also considers
priority assigned to a element.
These priorities are assigned based on a function given by user of priority queue.

Elements will be added directly to the priority queue without considering its
priority. But while removing elements we will first calculate element with highest
priority and that element will be removed.
"""

class Task:
    __slot__ = 'name', 'timeLeft'

    def __init__(self, name, timeLeft):
        self.name = name
        self.timeLeft = timeLeft

    def after(self, task):
        return self.timeLeft > task.timeLeft

    def getName(self):
        return self.name

    def getTimeLeft(self):
        return self.timeLeft

    def __eq__(self, other):
        return self.timeLeft == other.timeLeft

    def __str__(self):
        return "(job: " + self.name + ", timeLeft: " + str(self.timeLeft) + ")"


class Node:
    __slots__ = 'data', 'next'

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getValue(self):
        return self.data


class PriorityQueue:

    __slot__ = 'afterFunction', 'head', 'last', 'size'

    def __init__(self, after):
        """
        Initialize a new empty priority queue.
        :param after: an ordering function. See definition of dequeue method.
        :return: None (constructor)
        """
        self.afterFunction = after
        self.head = None
        self.last = None
        self.size = 0


    def after(self, a, b):
        """
        This function uses comparison function given by user to determine which
        element should be removed first (among the one given as argument)
        :param a:     First element for comparison
        :param b:     Second element for comparison
        :return:    True if a should be removed before b else False
        """
        val1 = a.data
        val2 = b.data
        return self.afterFunction(val1, val2)

    def __str__(self):
        """
        Return a string representation of the contents of
        this priority queue, front value first.
        :return: String of all the elements of priority queue
        """
        ptr = self.head
        string = ""
        while ptr is not None:
            string += str(ptr.data) + " "
            ptr = ptr.next
        return string

    def enqueue(self, newValue):
        """
        Enter a new value into the queue.
        :param newValue: the value to be entered into the queue
        :return: None
        """
        newNode = Node(newValue)
        if self.head is None:
            self.head = newNode
            self.last = self.head
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1

    def isEmpty(self):
        """
        :return: True iff there are no elements in the queue.
        """
        return self.head == None

    def getRemovableElement(self):
        """
        This method will return reference of the node that would be removed next.
        This will traverse priorityqueue and try to find that element using
        after function given by user.
        :return:    Reference of the node that would be removed next.
        """
        ptr = self.head.next
        remove = self.head
        while ptr is not None:
            while not self.after(remove, ptr):
                if ptr.next is not None:
                    ptr = ptr.next
                else:
                    return remove
            if remove.data.__eq__(ptr.data):
                ptr = ptr.next
            else:
                remove = ptr
                ptr = ptr.next
        return remove

    def peek(self):
        """
        Find in the queue the value that would be removed were the dequeue
        method to be called at this time.
        :pre: not isEmpty()
        :return: the value described above
        """
        return self.getRemovableElement().getValue()

    def dequeue(self):
        """
        Remove one of the values v from the queue such that,
        for all values u in the queue, after(v,u) is False.
        If more than one value satisfies the requirement,
        the value chosen should be the one that has
        been in the queue the longest.
        :pre: not isEmpty()
        :return: None
        """
        ptr = self.getRemovableElement()
        if ptr == self.head:
            self.head = self.head.next
        else:
            ptr2 = self.head
            while ptr2.next != ptr:
                ptr2 = ptr2.next
            ptr2.next = ptr.next
            ptr.next = None
        self.size -= 1

    remove = dequeue
    insert = enqueue



def after(a, b):
    """
    Test function for comaprison
    :param a:     first element for comparison
    :param b:     second element for comparison
    :return:      True if a is greater than b else False
    """
    return a > b


def testForInt():
    """
    This is a test function for integers.
    This will add few integers and the call peek and dequeue methods to update the
    priority queue.
    :return: None
    """
    pq = PriorityQueue(after)
    print("adding 1")
    pq.enqueue(1)
    print("adding 4")
    pq.enqueue(4)
    print("adding 2")
    pq.enqueue(2)
    print("adding 3")
    pq.enqueue(3)
    print("adding 6")
    pq.enqueue(6)
    print("adding 2")
    pq.enqueue(2)
    print(pq)
    ptr = pq.peek()
    print("pq.peek() : ", str(ptr))
    print("Removing ", str(ptr))
    pq.dequeue()
    ptr = pq.peek()
    print("pq.peek() : ", ptr)
    print("Removing ", str(ptr))
    pq.dequeue()
    print("adding 1 again")
    pq.enqueue(1)
    ptr = pq.peek()
    print("pq.peek() : ", str(ptr))
    print("Removing ", str(ptr))
    pq.dequeue()
    print(pq)

def testForTask():
    """
    This is a test function for
    :return:
    """
    taskPQ = PriorityQueue(Task.after)
    taskPQ.insert(Task('a', 8))
    taskPQ.insert(Task('b', 4))
    taskPQ.insert(Task('c', 3))
    taskPQ.insert(Task('d', 2))
    taskPQ.insert(Task('e', 5))
    taskPQ.insert(Task('f', 2))
    print(taskPQ)
    ptr = taskPQ.peek()
    print("taskPQ.peek(): " + ptr.name)
    print("removing job: " + ptr.name)
    taskPQ.remove()
    ptr = taskPQ.peek()
    print("taskPQ.peek(): " + ptr.name)
    print("removing job: " + ptr.name)
    taskPQ.remove()
    ptr = taskPQ.peek()
    print("taskPQ.peek(): " + ptr.name)
    print("removing job: " + ptr.name)
    taskPQ.remove()
    ptr = taskPQ.peek()
    print("taskPQ.peek(): " + ptr.name)
    print("removing job: " + ptr.name)
    taskPQ.remove()
    print(taskPQ)

if __name__ == '__main__':
    print("--------------- Test for int ---------------")
    testForInt()
    print("--------------- Test for task ---------------")
    testForTask()
