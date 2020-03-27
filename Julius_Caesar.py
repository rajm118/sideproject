a = int(input("Enter the value of key/shift"))
temp = []
temp2 = []
for i in range(ord('a'), ord('z') + 1):
    temp.append(chr(i))
for i in range(ord('a') + a, ord('z') + 1 + a):
    if i < 122:
        temp2.append((chr(i)))
    else:
        i = i % 122 + 97
        temp2.append(chr(i))
dic = {}
for i in range(26):
    dic.update({temp[i]: temp2[i]})

state = input("Enter the string that you want to convert ")
final = list(state)
counter = 0
for i in range(len(state)):
    final[counter] = dic.get(final[i])
    counter = counter + 1
final = str(final)

print("The Encoded string ",final)