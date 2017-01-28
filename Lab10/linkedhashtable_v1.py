__author__ = 'Pratik'

import collections
from set import SetType

MIN_BUCKETS = 10

class LinkedHashTable (SetType, collections.Iterable):
    __slots__ = "front", "back", "size", "load_limit", "table", "copacity", "prevAdded"

    def __init__(self, size = 100, load_limit = 0.75):
        """
        Create a new empty hash table.
        :param initial_num_buckets: starting number_of_buckets
        :param load_limit: See class documentation above.
        :return:
        """
        SetType.__init__(self)
        if (size < MIN_BUCKETS):
            size = MIN_BUCKETS
        self.size = size
        self.front = None
        self.back = None
        self.load_limit = load_limit
        self.table = [None for _ in range(self.size)]
        self.copacity = 0
        self.prevAdded = None

    def add( self, obj ):
        """
        Insert a new object into the hash table and remember when it was added
        relative to other calls to this method. However, if the object is
        added multiple times, the hash table is left unchanged, including the
        fact that this object's location in the insertion order does not change.
        Double the size of the table if its load_factor exceeds the load_limit.
        :param obj: the object to add
        :return: None
        """
        if self.copacity > int(self.load_limit * self.size):
            self.rehash(0)
        index = self.getLocation(self.getHash(obj))
        self.insertAt(index, obj)
        self.copacity += 1

    # TODO
    # write a check function like hashSet
    def insertAt(self, index, obj):
        newElement = ChainNode(obj)
        element = self.table[index]
        if element is None:
            self.table[index] = newElement
            if self.prevAdded is not None:
                self.prevAdded.link = newElement
                newElement.prev = self.prevAdded
            self.prevAdded = newElement
        else:
            if element.obj == obj:
                return
            else:
                e = self.getObjectPositionInList(element, obj)
                if e.obj == obj:
                    return
                else:
                    e.chain = newElement
                    self.prevAdded.link = newElement
                    newElement.prev = self.prevAdded
                    self.prevAdded = newElement
        if self.copacity == 0:
            self.front = newElement
        self.back = newElement

    def getObjectPositionInList(self, element, obj):
        while element.chain is not None:
            element = element.chain
            if element.obj == obj:
                break
        return element


    def contains( self, obj ):
        """
        Is the given obj in the hash table?
        :return: True iff obj or its equivalent has been added to this table
        """
        index = self.getLocation(self.getHash(obj))
        element = self.table[index]
        if element is None:
            return False
        if element.obj == obj:
            return True
        e = self.getObjectPositionInList(element, obj)
        if e.obj == obj:
            return True
        return False

    def remove( self, obj ):
        """
        Remove an object from the hash table (and from the insertion order).
        Resize the table if its size has dropped below
        (1-load_factor)*current_size.
        :param obj: the value to remove; assumes hashing and equality work
        :return:
        """
        if self.copacity < ((1-self.load_limit) * self.size):
            self.rehash(1)
        index = self.getLocation(self.getHash(obj))
        element = self.table[index]
        if element is None:
            return None
        if element.obj == obj:
            if self.front == element:
                self.front = element.link
            if element.prev is not None:
                element.prev.link = element.link
            self.table[index] = element.chain
        else:
            e = self.getObjectPositionInList(element, obj)
            if e.obj == obj:
                e.prev.link = e.link
                replaceE = self.table[index]
                while replaceE.chain != e:
                    replaceE = replaceE.chain
                replaceE.chain = e.chain
        self.copacity -= 1



    def __iter__(self):
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
        # currentElement = self.front
        # while currentElement is not None:
        #     yield currentElement.obj
        #     currentElement = currentElement.link
        return LinkedHashTableIterator(self.front, self.back)



    def getHash(self, obj):
        """
        Returns new hash value as hash of given object multiplied
        by 31
        :param obj:    Object who's hash value is to be found
        :return:    new hash value of object
        """
        return obj.__hash__() * 31

    def getLocation(self, hash):
        """
        Returns a integer that is the location of the given object in the table
        :param hash: hash value of the object
        :return:    location of the object in the table
        """
        return hash & (self.size - 1)

    def rehash(self, option):
        if option == 0:
            self.size *= 2
            front = self.front
            back = self.back
            self.front = None
            self.back = None
            self.table = [None for _ in range(self.size)]
            self.copacity = 0
            self.prevAdded = None
            e = front
            while e is not None and e is not back:
                self.add(e.obj)
                e = e.link
            self.add(back.obj)
        elif option == 1:
            if self.size // 2 >= MIN_BUCKETS:
                self.size //= 2
                front = self.front
                back = self.back
                self.front = None
                self.back = None
                self.table = [None for _ in range(self.size)]
                self.copacity = 0
                self.prevAdded = None
                e = front
                while e is not None and e is not back:
                    self.add(e.obj)
                    e = e.link
                self.add(back.obj)



class ChainNode (object):
    __slots__ = "obj", "link", "prev", "chain"

    def __init__(self, obj, prev=None, link=None, chain=None):
        self.obj = obj
        self.link = link
        self.prev = prev
        self.chain = chain

    def __str__(self):
        return str(self.obj)

class LinkedHashTableIterator(collections.Iterator):
    __slots__ =  "currentElement", "back"

    def __init__( self,front, back ):
        self.currentElement = front
        self.back = back

    def __next__( self ):
        element = self.currentElement
        if self.currentElement is None:
            raise StopIteration()
        if self.currentElement is not None:
            self.currentElement = self.currentElement.link
            return element.obj