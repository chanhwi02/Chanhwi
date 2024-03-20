# 0부터 40까지 더하기
iend = 20
total = 0

for i in range(iend):
    i+1
    total = total + 2 * (i+1)
print(total)

# while은 조건을 만족하면 밑에 블록을 실행

i = 0
total = 0
while i < 20:
    i=i+1
    total = total + i
print(total)

# for <-> while문 바꾸기 시험문제!

for m in ["사과", "배", "복숭아", "자몽", "캐슈넛"]:
    if m not in ["캐슈넛"]:
        print("나는",m,"을(를) 좋아합니다.")

# i가 의미없는 경우 _로 대체해도 됨
for _ in range(100):
    print("I like you")







numbers = [11, 22, 33, 44, 55, 66]

for n in numbers:
    print(n, end = '\n')
# print(n, end = "")와 print(n)은 다름
