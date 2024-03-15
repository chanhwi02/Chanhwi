# 두 개의 정수를 입력하여 배수인지 확인 if 조건문 사용
a,b=map(int,input("두 개의 정수를 입력해주세요:").split())
if a%b == 0:
    print("{0:d}은(는) {1:d}의 배수입니다".format(a,b))
# format은 위치지정 하는 것
# d는 '정수를 써라' 라는 뜻
