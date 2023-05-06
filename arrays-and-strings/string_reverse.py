
def reverse(s):
    left_indx = 0
    right_indx = len(s) - 1
    rs = []
    str1 = ""

    while right_indx >= 0:
        rs.insert(left_indx, s[right_indx])
        left_indx = left_indx + 1
        right_indx = right_indx - 1

    return str1.join(rs)


input_str = "hello"
print('Original string is:{} and the reversed string is:{}'.format(input_str,reverse(input_str)))
