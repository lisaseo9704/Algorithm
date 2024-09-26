num = int(input())
num_list = input().split()
int_list = [int(i) for i in num_list]
int_list.sort()
print(int_list[0]*int_list[-1])