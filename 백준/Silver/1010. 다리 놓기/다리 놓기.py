import math

num = int(input())

for _ in range(num):
  left, right = map(int, input().split())
  if left > right:
    print(math.comb(left,right))
  else:
    print(math.comb(right,left))