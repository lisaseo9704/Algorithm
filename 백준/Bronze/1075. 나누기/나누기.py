number = int(input())
div_num = int(input())

new_num = (number//100)*100

while (new_num%div_num!=0):
  new_num += 1

last_two_digits = new_num % 100
print(f'{last_two_digits:02}')