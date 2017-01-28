"""
# file: tests.py
# description: Verify the LinkedHashTable class implementation
# """

__author__ = [ "Pratik" ]

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set: # uses the iter method
        print( word, end=" " )
    print()

def test0():
    table = LinkedHashTable( 100 )
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print_set( table )

    print( "'to' in table?", table.contains( "to" ) )
    table.remove( "to" )
    print( "'to' in table?", table.contains( "to" ) )

    print_set( table )


def test1():
    allGood = True
    table = LinkedHashTable( 1 )
    string = "batman has lots of gizmos in his belt"
    stringset = string.split(" ")
    for i in stringset:
        table.add(i)
    print("table: ", end= " ")
    print_set(table)
    for j in stringset:
        if table.contains(j) is False:
            print("OMG!")
            allGood = False
    print("allGood: " + str(allGood))
    for j in stringset:
        table.remove(j)
    print("table: ", end= " ")
    print_set(table)



def test2():
    string = "to to to to are four to's"
    print("String being added: " + string)
    allGood = True
    table = LinkedHashTable( 100 )
    stringset = string.split(" ")
    for i in stringset:
        table.add(i)
    print("table: ", end= " ")
    print_set(table)
    table.remove("to")
    print( "'to' in table?", table.contains( "to" ) )
    print("table: ", end= " ")
    print_set(table)

def test3():
    string = "abcd"
    table = LinkedHashTable( 100 )
    for i in range(10):
        table.add(string + str(i))
    print("table: ", end= " ")
    print_set(table)
    print("**************************************************************")
    for s in table:
        table.remove(s)
        print("----------------------------------------------------------")
        print("table: ", end= " ")
        print_set(table)
    for i in range(10):
        table.add(i)
    print("table: ", end= " ")
    print_set(table)
    print("**************************************************************")
    for s in table:
        table.add(s)
        print("----------------------------------------------------------")
        print("table: ", end= " ")
        print_set(table)
    print("is 10 in?" + str(table.contains(10)))




if __name__ == '__main__':
    # test0()
    # test1()
    # test2()
    test3()
