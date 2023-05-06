def check_if_palindrome(s):
    left_indx = 0
    right_indx = len(s) - 1

    flag = True
    while left_indx <= right_indx:
        if s[left_indx] == s[right_indx]:
            left_indx = left_indx + 1
            right_indx = right_indx - 1
        else:
            flag = False
            break
    return flag


input_str = "12321"
print(check_if_palindrome(input_str))
