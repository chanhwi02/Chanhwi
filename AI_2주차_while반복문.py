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
print(total)
# 시험에는 for이나 while 중 하나를 주고 나머지 하나로 바꾸라고 함

# while 반복문 2
total=0
for i in range(10):
    total+=i
total = 0
i = 0
while True:
    total+=i
    i+=1
    if(i>=10) break
print(total)

# 원래 True를 넣으면 무한루프
# 그러나 if(i>=10) break를 넣으면 10 이상이 되면 멈춤

total = 0
for i in range(10):
    total+=i
total = 0
i = 0
while i<10:
    if i%3 ==0:
    continue
    total + = i
    i+=1
print(total)
# 3의 배수는 더하지 마라
