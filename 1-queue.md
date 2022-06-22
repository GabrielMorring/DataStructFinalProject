# Queues

## Explanation

A queue is a data structure where the first in is the first out. If you think of a line at an amusement park, the people who got in before you will get on the ride before you. Queues work the same way where the data gets read from the queue in the same order that it got put in. When you add something to a queue it is called **Enqueue** and when you remove it is called **Dequeue**.

Queues are useful when you need to keep track of the order of data. An example of when a queue would be good to use is at a resturant to keep track of peoples orders, you would enqueue peoples orders to the queue when they make them and dequeue thier order when you serve them. that way the resturant would make sure they are serving their customers in the same order they came in.

A queue is used in python with a python list. You use a python list as a queue by only adding items to the list on one side and only removing from the other. You would only add to the back of the list and only remove from the front.

### Queue Operations In Python

| Operation | Python code    | Performance                                                                                 |
| --------- | -------------- | ------------------------------------------------------------------------------------------- |
| Enqueue   | queue.append() | O(1) just adding to the end of a list.                                                      |
| Dequeue   | queue.pop(0)   | O(n) because you need to shift all the items over when you remove from the front of a list. |

## Example

Here is an example of a queue being used in a program

```python
'''
I have a hard time focusing on one thing at a time so i made a
simple to do program where you enter all the things that you
have to do and it tells you them one at a time to help me focus
on just that thing.

'''

to_do = []

print()
print('To do app')
print()

print('Instructions: Enter all the tasks you want to complete')
print('then do the tasks when that the program tells you to do.')

print()
print("Enter your tasks:")
print()

ans = '0'

while ans != '3':

    print('0. Enter task')
    print('1. Do Task')
    print('3: quit')

    ans = input(': ')

    if ans == '0':
        to_do.append(input('Task: '))
    elif ans == '1':

        if len(to_do) != 0:
            print()
            print(to_do.pop(0))
            print()
            input('press enter to continue:')

        else:
            print()
            print('You don\'t have any tasks to complete')
            print()

    elif ans == '3':
        print("Goodbye")

    else:
        print('You must enter one of the numbers.')
```

You can view the python file [here](./python/queue-example.py)

## Problem to solve
