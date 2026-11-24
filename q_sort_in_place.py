def quicksort_i(start_idx, end_idx, num_list):
    if (end_idx-start_idx+1) > 0:
        pivot_idxes = [start_idx, (start_idx+end_idx)//2, end_idx]
        pivot_list = []

        for i in pivot_idxes:
            pivot_list.append(num_list[i])  

        pivot_val = sum(pivot_list) - max(pivot_list) - min(pivot_list)
        pivot_idx = pivot_idxes[pivot_list.index(pivot_val)]

        num_list[pivot_idx], num_list[start_idx] = num_list[start_idx], num_list[pivot_idx]

        f = start_idx+1
        r = end_idx
        pivot_idx = start_idx
        
        while f <= r:
            while num_list[r] > num_list[pivot_idx]:
                r -= 1
            
            while f <= r and num_list[f] < num_list[pivot_idx]:
                f += 1

            if f <= r:
                num_list[f], num_list[r] = num_list[r], num_list[f]

        num_list[r], num_list[pivot_idx] = num_list[pivot_idx], num_list[r]

        print(num_list)
        # print(f"{' ' * start_idx}{num_list[start_idx:end_idx+1]}{' ' * (len(num_list)-end_idx-1)}")

        quicksort_i(start_idx, r-1, num_list)
        quicksort_i(r+1, end_idx, num_list)

if __name__ == '__main__':
    n = int(input())
    num_list = []

    for _ in range(n):
        num_list.append(int(input()))

    quicksort_i(0, n-1, num_list)

    for num in num_list:
        print(num)