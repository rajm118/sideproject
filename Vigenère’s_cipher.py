text = input("Enter The text to be encrypted :")
key_ = input("Enter the key :")
text.lower()
key_.lower()
dic = {}
temp2 = []

ans = []
for i in range(ord('a'), ord('z') + 1):
    dic.update({chr(i): i - 97})
for i in range(len(text)):
    temp = i % len(key_)
    ans.append((dic.get(text[i]) + dic.get(key_[temp])) % 26)

    print(ans,dic.get(text[i]), dic.get(key_[temp]),temp)
for i in range(len(text)):
    for key, value in dic.items():
        if ans[i] == value:
            temp2.append(key)
str(temp2)
print(temp2)
print(ans)