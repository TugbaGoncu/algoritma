# def is_palindrome(sayı):
#     reverse_sayı = sayı[::-1]
#     if sayı == reverse_sayı:
#         return True
#     else:
#         return False
#
# sayı = input("Bir sayı girin: ")
# if is_palindrome(sayı):
#     print("Bu bir palindrom sayıdır.")
# else:
#     print("Bu bir palindrom sayı değildir.")
#https://leetcode.com/problems/palindrome-linked-list/
def is_palindrome(head):
    reverse_sayılar = head[::-1]
    if head == reverse_sayılar:
        return True
    else:
        return False
head = [1, 2, 2, 3]
if is_palindrome(head):
    print("Bu bir palindrom sayılar listesidir.")
else:
    print("Bu bir palindrom sayılar listesi değildir.")