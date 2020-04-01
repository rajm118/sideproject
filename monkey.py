from random import randrange

# trying out infinte monkey thoerem

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
final = input(" !!!! CAUTION !!!!! \n longer the sequence longer will be the time required \n Enter the sequence :")
final.upper()


def monkey():
    temp=""
    for i in range(len(final)):
        temp += LETTERS[randrange(len(LETTERS))]
    return temp
if __name__ == '__main__':
    flag = 0
    counter = 0
    while flag != 1:
        temp=monkey()
        counter = counter + 1
        print(temp)
        if temp == final:
            flag = 1
    print("match found after ", counter, " iterations")
