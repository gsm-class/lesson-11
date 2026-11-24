def combine(f_list, r_list):
    f_idx = 0
    r_idx = 0
    combined_list = []

    while f_idx < len(f_list) and r_idx < len(r_list):
        if f_list[f_idx] <= r_list[r_idx]:
            combined_list.append(f_list[f_idx])
            f_idx += 1
        else:
            combined_list.append(r_list[r_idx])
            r_idx += 1

    combined_list += f_list[f_idx:len(f_list)]
    combined_list += r_list[r_idx:len(r_list)]

    return combined_list

def merge_sort(start_idx, end_idx, num_list):
    if start_idx >= end_idx:
        return num_list[start_idx:end_idx+1]

    mid_idx = (start_idx+end_idx) // 2

    f_sorted_list = merge_sort(start_idx, mid_idx, num_list)
    r_sorted_list = merge_sort(mid_idx+1, end_idx, num_list)

    return combine(f_sorted_list, r_sorted_list)

if __name__ == '__main__':
    n = int(input())
    num_list = []

    for _ in range(n):
        num_list.append(int(input()))

    sorted_list = merge_sort(0, n-1, num_list)

    for num in sorted_list:
        print(num)

