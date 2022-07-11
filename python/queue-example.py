'''
I have a hard time focusing on one thing at a time so i made a
simple to do program where you enter all the things that you
have to do and it tells you them one at a time to help you focus on
just that thing.
'''

from collections import deque

to_do = deque()

print()
print('To do app')
print()

print('Instructions: Enter all the tasks you want to complete')
print('then do the tasks that the program tells you to do.')

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
            print(to_do.popleft())
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