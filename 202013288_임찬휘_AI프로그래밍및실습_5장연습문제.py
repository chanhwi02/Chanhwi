# 202013288 임찬휘 AI프로그래밍및실습 5장 연습문제

# 연습문제 5.1
# (1)
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
list_ex[low]
# >>> 40

# (2)
list_ex[low + 2]
# >>> 60

# (3)
list_ex[high-low]
# >>> 30

# (4)
list_ex[low-high]
# >>> 60

# (5)
list_ex[-1]
# >>> 70

# (6)
list_ex[-low]
# >>> 50

# (7)
list_ex[2 * 3]
# >>> 70

# (8)
list_ex[2] * 3
# >>> 90

# (9)
list_ex[5 % 4]
# >>> 20

# (10)
len(list_ex)
# >>> 7


# 연습문제 5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]
for i in list1:
    for j in list2:
        print('{} * {} = {}'.format(i, j, i * j))
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
​
# 연습문제 5.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']
for i in list1:
    for j in list2:
        print('{} {}'.format(i, j))

# 연습문제 5.7
n_list = [10, 20, 30, 50, 60]

v_sum = 0
for i in n_list:
    v_sum += i
print(v_sum)

# 연습문제 5.9
v_max = 0
for i in n_list:
    if i > v_max:
        v_max = i
print(v_max)

# 연습문제 5.11
List = list(map(int, input('5개의 수를 입력하세요: ').split()))
print('합: {}'.format(sum(List)))
print('평균: {}'.format(sum(List) / len(List)))
print('최댓값: {}'.format(max(List)))
print('최솟값: {}'.format(min(List)))

# 연습문제 5.13
nums = list(map(int, input('10개의 수를 입력하세요: ').split()))
print('합 :', sum(nums))
nums_average = sum(nums) / len(nums)
print('평균 :', nums_average)
nums_sigma = 0
for i in nums:
    nums_sigma += (i - nums_average) ** 2
print('표준편차 : {:.2f}'.format((nums_sigma / len(nums)) ** 0.5))

# 연습문제 5.15
greet = 'Have a beautiful day.'
greet[0:4]
greet[7:16]
greet[17:20]

# 연습문제 5.17
# (1)
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
# (2)
animals.append(animals.pop(0))
print('animals : {}'.format(animals))
# (3)
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals : {}'.format(animals))
for i in animals:
    print('I love {}.'.format(i))

# 연습문제 5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = list(set(s_list))

print(s_list)
print(new_s_list)

# 연습문제 5,21
src = 'a2b3c6a2c3f1g1'
print(src)

for ch in src:
  if ch.isnumeric():
    for i in range(int(ch)):
      print(ch_old,end='')
  else:
    ch_old = ch

# 연습문제 5.23
person1 =['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

def function_of_persons(person_list):
    result = {}
    divide_list = []
    for i in range(int(len(person_list) / 5)):
        divide_list.append(person_list[i * 5:i * 5 + 5])
    result['n_persons'] = len(divide_list)
    result['average_age'] = 0
    result['n_male'] = 0
    result['f_male'] = 0
    result['person_list'] = divide_list
    for i in divide_list:
        result['average_age'] += i[1]
        if i[2] == 1:
            result['n_male'] += 1
        else:
            result['f_male'] += 1
    result['average_age'] /= result['n_persons']
    return result
    
person_list = person1 + person2 + person3 + person4
print(function_of_persons(person_list))
