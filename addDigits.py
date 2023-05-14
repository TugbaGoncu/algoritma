
#https://leetcode.com/problems/add-digits/
num = input("sayı giriniz:")

def addDigits(num):
    while True:
        if len(num) == 2:
            print("541d5")
            print(type(num))
            num = int(num[0]) + int(num[1])
            print(num)
            num = str(num)
            print(len(num))
            if len(num) == 1:
                print("tek rakam indirildi")
                break
            elif len(num) == 2:
                num = int(num[0]) + int(num[1])
                print(num)
                break
            break
        elif len(num) == 1:
            print(num)
            break

addDigits(num)
