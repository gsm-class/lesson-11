n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

target_size = 1

while target_size < n:
    start_idx = 0

    # TODO: 여기에 코드를 작성 하세요.

    target_size *= 2

if __name__ == '__main__':
    for num in num_list:
        print(num)