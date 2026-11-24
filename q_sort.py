def quicksort(num_list):

    # TODO: 여기에 코드를 작성하세요.

    return quicksort(less_list) + [num_list[pivot_idx]] + quicksort(more_list)

if __name__ == '__main__':
    n = int(input())
    num_list = []

    for _ in range(n):
        num_list.append(int(input()))

    for num in quicksort(num_list):
        print(num)