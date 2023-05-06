
def find_sum_pairs(lst, tgt_sum):
    left_indx = 0
    right_indx = len(lst) - 1
    num_pairs = set()

    while left_indx < right_indx:
        if lst[left_indx] + lst[right_indx] > tgt_sum:
            right_indx = right_indx - 1
        elif lst[left_indx] + lst[right_indx] < tgt_sum:
            left_indx = left_indx + 1
        else:
            num_pairs.add(lst[left_indx])
            num_pairs.add(lst[right_indx])
            break
    return num_pairs


input_list = [ 1,2,3,4,5,6,7,8]
num_pairs = find_sum_pairs(input_list,9)
print(num_pairs)

