"""
taskmaster.py

Demonstrate Priority-queue based task lists.
author: James Heliotis
author: Pratik Kulkarni
"""

from prioqueue import PriorityQueue as Dispenser

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

TICK_CMD = "tick"
ADD_CMD = "add"
QUIT_CMD = "quit"
COMMANDS = ( TICK_CMD, ADD_CMD, QUIT_CMD )

def main():

    tasks = Dispenser(Task.after)
    time = 0

    cmd, args = get_cmd( COMMANDS )
    while cmd != QUIT_CMD:
        if cmd == TICK_CMD:
            time += 1
            if not tasks.isEmpty():
                current = tasks.peek()
                current.timeLeft -= 1
                if current.timeLeft == 0:
                    print( "\nTask '" + current.name + \
                           "' completed at time " + str( time ) + "." )
                    tasks.remove()
                    if not tasks.isEmpty():
                        print( "New task is '" + tasks.peek().name + "'." )
                    else:
                        print( "Nothing else to do." )
            else:
                print( "Nothing to do." )
        elif cmd == ADD_CMD:
            new_task = Task( args[ 0 ], int( args[ 1 ] ) )
            tasks.insert( new_task )
            print(tasks)
            print( "\nAdded. Current task is '" + tasks.peek().name + \
                   "'." )
        else:
            assert True, "PROGRAM ERROR"
        cmd, args = get_cmd( COMMANDS )

    print( "\nTerminating the simulation." )

def get_cmd( choices ):
    line = input( "\nEnter one of " + str( choices ) + ": " ).split()
    cmd = line.pop( 0 )
    while cmd not in choices:
        print( "\n'" + cmd + "' is not a legal command. Try again." )
        line = input( "\nEnter one of " + str( choices ) + ": " ).split()
        cmd = line.pop( 0 )
    return cmd, line

if __name__ == "__main__":
    main()
