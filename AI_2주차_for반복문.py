total=0
numbers = [10, 20, 30, 40, 50]

# number에 있는 숫자 하나씩 m이 된다
# 루프가 돌아가면서 m에 숫자가 하나씩 들어감
for m in numbers:
    total=total+m
print(total)

# while 반복문
# while은 조건이 좀 더 명확하다
total=0
for i in range(10):
    total+=i
# i가 10보다 작으면 계속 반복하라는 뜻
total = 0
i = 0
while i<10:
    total+=i
    i+=1
# 시험에는 for이나 while 중 하나를 주고 나머지 하나로 바꾸라고 함
