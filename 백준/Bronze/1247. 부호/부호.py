for _ in range(3):
  num = int(input())
  sum = 0
  for _ in range(num):
    sum += int(input())

  if sum == 0:
    print('0')
  elif sum > 0:
    print('+')
  else:
    print('-')