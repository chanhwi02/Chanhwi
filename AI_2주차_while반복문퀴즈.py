total = 0
for i in range(10):
    total+=i
total = 0
i = 0
while i<9:
    i += 1
    if i%3 ==0: continue
    total += i
print(total)
# 3의 배수는 제외하고 더하기
