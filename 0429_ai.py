class comx:
    def __init__(self,x,y):
        self.real = x
        self.imag = y
    def __add__(self,b):
        return comx(self.real+b.real, self.imag+b.imag)
    def __mul__(self,b):
        return comx(self.real*b.real-self.imag*b.imag, self.imag*breal+self.real*b.imag)
    def __str__(self,b):
        return "({}, {})".format(self.real, b.real)
        

a = comx(1,2)
b = comx(2,3)
c = a + b
d = a * b
print(c)
print(d)

# 2
def imax(*a):
    max_value = a
    if b > max_value : max_value = b
    if b > max_value : max_value = b
        
    return max_value
imax(10, 200, 30)



# 3
class human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        print('내 이름은 {}, 나이는 {}, 성별은 {}'.format(self.name, self.age, self.sex))
    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self. sex = sex
    # del는 변수 지우기 가능
    def __del__(self):
        print("{}의 죽음을 알리지마라.".format(self.name))
noah = human("영호", 28, "남자")

noah.setinfo("상규", 24, "남자")

del(noah)
