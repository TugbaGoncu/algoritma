# https://leetcode.com/problems/merge-two-sorted-lists/

list1 = [1,2,4]
list2 = [1,3,4]

def mergeTwoShordetLists(list1,list2):
    list3=list1+list2
    list3.sort(reverse=False)
    print(f'{list3}')
mergeTwoShordetLists(list1,list2)
