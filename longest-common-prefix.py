#https://leetcode.com/problems/longest-common-prefix/
strs = ["flower", "flow", "flight"]

def countChars(word):
    chars = {}
    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


char_counts = [countChars(word) for word in strs]


common_chars = []
for char in char_counts[0]:
    is_common = True
    for i in range(1, len(char_counts)):
        if char not in char_counts[i]:
            is_common = False
            break
    if is_common:
        common_chars.append(char)


print(f"Ortak karakterler: {common_chars}")