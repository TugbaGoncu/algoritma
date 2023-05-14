#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
digits=input("telefon numarası:")
list={2:'abc',3:'def',4:'ghi',}
list2=[]
def letterOfAPhoneNumber(digits,list):
    if len(digits)==0:
        print(digits[0])
    elif len(digits)==1:
        print(digits[0])
    elif len(digits)==2:
        a= digits[0]
        b= digits[1]
        aValue=list[int(a)]
        bValue=list[int(b)]
        for i in range(3):
            c=aValue[i]+bValue[len(bValue)-1]
            print(c)
            list2.append(c)
            #print(aValue[len(aValue)//2)
    print(list2)


letterOfAPhoneNumber(digits,list)
# d = {18:'alice'}
# keys = ['carl', 'bob']
# a=(d[18])
# print(a[0])