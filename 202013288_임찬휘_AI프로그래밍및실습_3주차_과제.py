# 202013288 임찬휘 AI프로그래밍및실습 연습문제 3번과제

# 연습문제 3.1
# (1) False
# (2) False
# (3) True
# (4) False
# (5) False
# (6) True
# (7) True
# (8) False
# (9) True
# (10) True
# (11) False
# (12) True
# (13) True
# (14) True
# (15) True
# (16) False


# 연습문제 3.3
age = int(input('나이를 입력하시오:'))
height = int(input('키를 입력하시오(단위 cm):'))
if age>=19 and height>=150:
    print('입장할 수 있습니다.')
else:
    print('입장할 수 없습니다.')

# 연습문제 3.5
a,b = map(int,input('두 정수를 입력하시오:').split())
if a > b:
    print('{0} {1}'.format(b,a))
else:
    print('{0} {1}'.format(a,b))

# 연습문제 3.7
score = int(input('게임점수를 입력하시오:'))
if score>=1000:
    print('고수입니다.')
else:
    print('입문자입니다.')

# 연습문제 3.9
number = int(input('정수를 입력하시오:'))
if number % 2 == 0:
    print(number,'는(은) 2(으)로 나누어집니다.')
else:
    print(number,'는(은) 2(으)로 나누어지지 않습니다.')

if number % 3 == 0:
    print(number,'는(은) 3(으)로 나누어집니다.')
else:
    print(number,'는(은) 3(으)로 나누어지지 않습니다.')

if (number % 2 == 0) and (number % 3 == 0):
    print(number,'는(은) 2와(과) 3 모두로 나누어집니다.')
else:
    print(number,'는(은) 2와(과) 3 모두로 나누어지지 않습니다.')

# 연습문제 3.11
a,b,c = map(int,input('세 복권번호를 입력하시오:').split())
if (a==2 and b==3 and c==9):
    print('1억 원')
elif (a!=2 and b==3 and c==9):
    print('1천만 원')
elif (a==2 and b!=3 and c==9):
    print('1천만 원')
elif (a==2 and b==3 and c!=9):
    print('1천만 원')
elif (a!=2 and b!=3 and c==9):
    print('1만 원')
elif (a==2 and b!=3 and c!=9):
    print('1만 원')
elif (a!=2 and b==3 and c!=9):
    print('1만 원')
else:
    print('다음 기회에...')

# 연습문제 3.13
x,y = map(int,input('점의 좌표 x,y를 입력하시오').split())
if (x-3)**2 + (y-4)**2 > 100:
    print('원의 외부의 있음')
else:
    print('원의 내부에 있음')

# 연습문제 3.15
for i in range(1,10,1):
    print("2 *" + str(i) + "=" + str(2*i))

# 연습문제 3.17

# 1)
for i in range(3):
    print('Python')
    print("is")
    print('FUN!')
# Python is FUN! Python is FUN! Python is FUN!

# 2)
for i in range(3):
    print('Python')
    print("is")
print('FUN!')
# Python is Python is Python is FUN!

# 연습문제 3.19
print('만나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('- 햄버거(입력 b) \n- 치킨(입력 c) \n- 피자(입력 p)')

menu = input('메뉴를 선택하세요(알파벳 b, c, p 입력) : ')
while menu not in ['b', 'c', 'p']:
    menu = input('메뉴를 다시 선택하세요(알파벳 b, c, p 입력) : ')

if menu == 'b':
    print('햄버거를 선택하였습니다.')
if menu == 'c':
    print('치킨을 선택하였습니다.')
if menu == 'p':
    print('피자를 선택하였습니다.')

# 연습문제 3.21
n = int(input('숫자를 입력하세요:'))
if n == 2:
    print(n,'은 소수입니다')
elif n % 2 == 0:
    print(n,'은 소수가 아닙니다')
else:
    for i in range(3, n-1,2):
        if n % i !=0:
            print(n,'은 소수입니다.')
        else:
            print(n,'은 소수가 아닙니다.')

# 연습문제 3.23
n = int(input('숫자를 입력하세요:'))
result = 0

for i in range(1, n+1):
    result += i**2
    
print(result)

# 연습문제 3.25
day = 0
location = 0

while True:
    day +=1
    location +=7
    if location >= 30:
        print('day:{} \t 달팽이의 위치 : {} 미터'.format(day,location))
        print('\n우물을 탈출하는데 걸린 날은 {}일 입니다.'.format(day))
        break
    print('day:{} \n달팽이의 위치:{}미터'.format(day,location))
    location -= 5

# 연습문제 3.27
num=[]

for i in range(100,1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a **3 + b**3 + c**3:
        num.append(i)
        
print('세 자리의 암스트롱 수 : {}'.format(num))

# 연습문제 3.29
a = 500

while True:
    a += int(input('충전 또는 사용한 연료를 +/- 기호와 함꼐 입력하시오:'))
    print('현재 탱크양은 {} 입니다.'.format(a))
    if a < 50:
        print('경고 : 연료가 10% 미만이니 충전하세요!'.format(a))
        break

# 연습문제 3.31
for i in range(1, 20001):
    s = 0 # 친화수의 초기값
    s1 = 0 # 친화수의 진약수의 합의 초기값
    for j in range(1,i): # 220의 진약수의 합(284)
        if i % j == 0:
            s = s + j
    for k in range(1,s): # 220의 진약수의 합(284)의 진약수의 합(220)
        if s % k == 0:
            s1 = s1 + k
    if i == s1 and i != s:
        print('{}의 친화수 {}'.format(i, s))
