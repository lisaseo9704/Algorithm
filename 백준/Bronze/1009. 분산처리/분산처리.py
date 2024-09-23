T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    
    if a % 10 == 0:
        print(10)
    else:
        last_digit = a % 10
        pattern = [last_digit]
        next_num = (last_digit * last_digit) % 10
        while next_num != pattern[0]:
            pattern.append(next_num)
            next_num = (next_num * last_digit) % 10
        
        print(pattern[(b - 1) % len(pattern)])