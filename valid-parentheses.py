#https://leetcode.com/problems/valid-parentheses/
def validParentheses(s):
    # found=False
    for i in s:
        if i=="(" and i==")":
            print(i)
            # for j in range(i+1,len(s)):
            #     if s[i] == "(" and s[j] == ")" :
            #         print("doğru")
            #         found = True
            #         break
            #     elif s[i] == "[" and s[j] == "]":
            #         print("doğru2")
            #         found=True
            #         break

        # if found:
        #     break


s="[{()]"
validParentheses(s)



# def validParentheses(s):
#     found=False
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
#             if (s[i] == "(" and s[j] == ")") or (s[i] == "[" and s[j] == "]") or (s[i] == "{" and s[j] == "}"):
#                 print("doğru")
#                 found = True
#                 break
#         if found:
#             break
#
#
# s="[]{}()"
# validParentheses(s)