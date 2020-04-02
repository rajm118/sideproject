stack = ['a', 'b', 'c']
flag = 0
while flag == 0:
    stack.append(input())
    print("Do you want to enter more type 0 else type 1")
    flag = int(input())

print('Initial stack')
print(stack)

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
flag = 0
while flag == 0:
    stack.pop()
    print("Do you want to pop more type 0 else type 1")
    flag = int(input())
print('\nStack after elements are poped:')
print(stack)
