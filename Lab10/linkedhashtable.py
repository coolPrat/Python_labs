"""
author: Pratik Kulkarni

CSCI-605 Lab 10 Linke hash table

This class represents a hash map that maintains the order of elements
in which they were added in the hash-table. minimum size of hashtable is 10
Depending upon insertion or removal size of hash-table is adjusted using a rehash
function
"""
import collections
from set import SetType

MIN_BUCKETS = 10

class LinkedHashTable (SetType, collections.Iterable):
    __slots__ = "front", "back", "size", "load_limit", "table", "__copacity", "__prevAdded"

    def __init__(self, initial_num_buckets=100, load_limit = 0.75):
        """
        Create a new empty hash table.
        :param initial_num_buckets: starting number_of_buckets
        :param load_limit: See class documentation above.
        :return:
        """
        SetType.__init__(self)
        if (initial_num_buckets < MIN_BUCKETS):
            initial_num_buckets = MIN_BUCKETS
        self.__copacity = initial_num_buckets
        self.front = None
        self.back = None
        self.load_limit = load_limit
        self.table = [None for _ in range(initial_num_buckets)]
        self.size = 0
        self.__prevAdded = None

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
        if self.size > int(self.load_limit * self.__copacity):
            self.rehash(0)
        index = self.getLocation(self.getHash(obj))
        self.insertAt(index, obj)

    def insertAt(self, index, obj):
        """
        this method will add given object at given index in hash-table.
        if the object is already present it will simply return without adding.
        :param index:     index in hash table
        :param obj:       object to add
        :return:
        """
        newElement = ChainNode(obj)
        element = self.table[index]
        if element is None:
            self.table[index] = newElement
            if self.__prevAdded is not None:
                self.__prevAdded.link = newElement
                newElement.prev = self.__prevAdded
            self.__prevAdded = newElement
            self.size += 1
        else:
            if element.obj == obj:
                return
            else:
                e = self.getObjectPositionInList(element, obj)
                if e.obj == obj:
                    return
                else:
                    e.chain = newElement
                    self.__prevAdded.link = newElement
                    newElement.prev = self.__prevAdded
                    self.__prevAdded = newElement
                    self.size += 1
        if self.size == 1:
            self.front = newElement
        self.back = newElement

    def getObjectPositionInList(self, element, obj):
        """
        This function will return a ChainNode which represents place
         for given object. i.e. either the chainNode after with given
         object must be added or the chainNode that holds given object.
        :param element:     First chainNode at given index
        :param obj:         the object to add
        :return:            ChainNode object
        """
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
        self.size -= 1
        if (self.size < ((1 - self.load_limit) * self.__copacity)):
            self.rehash(1)



    def __iter__(self):
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
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
        return hash & (self.__copacity - 1)

    def rehash(self, option):
        """
        This method will reduce or increase the copacity of hash table
        based on option passed.
        0: increase
        1: reduce
        :param option:     indicates whether we need to increase or reduce the size
        :return:
        """
        if option == 0:
            self.__copacity *= 2
            front = self.front
            back = self.back
            self.front = None
            self.back = None
            self.table = [None for _ in range(self.__copacity)]
            self.size = 0
            self.__prevAdded = None
            e = front
            while e is not None and e is not back:
                self.add(e.obj)
                e = e.link
            self.add(back.obj)
        elif option == 1:
            if self.__copacity // 2 >= MIN_BUCKETS:
                self.__copacity //= 2
                front = self.front
                back = self.back
                self.front = None
                self.back = None
                self.table = [None for _ in range(self.__copacity)]
                self.size = 0
                self.__prevAdded = None
                e = front
                while e is not None and e is not back:
                    self.add(e.obj)
                    e = e.link
                self.add(back.obj)
                if (self.size < (self.load_limit * self.__copacity)):
                    self.rehash(1)

"""
This class represents a node in hash table.
It has pointers that link a given node with
1) a node that came before given node in hash table
2) a node that came after given node in hash table
3) a node that came after given node in given chain
"""
class ChainNode (object):
    __slots__ = "obj", "link", "prev", "chain"

    def __init__(self, obj, prev=None, link=None, chain=None):
        self.obj = obj
        self.link = link
        self.prev = prev
        self.chain = chain

    def __str__(self):
        return str(self.obj)

"""
This class represents a Iterator for LinkedHashTable
"""
class LinkedHashTableIterator(collections.Iterator):
    __slots__ =  "currentElement", "back"

    def __init__( self,front, back ):
        """
        Initialize iterator with front and bak pointer of  hash-table
        :param front:     Front pointer of hash table
        :param back:      Back pointer of hash table
        :return:
        """
        self.currentElement = front
        self.back = back

    def __next__( self ):
        """
        Returns next element in the LikedHashTable
        :return:    next element in the LikedHashTable
        """
        element = self.currentElement
        if self.currentElement is None:
            raise StopIteration()
        if self.currentElement is not None:
            self.currentElement = self.currentElement.link
            return element.obj
