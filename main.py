 #1 задание
numbers=int(input("введите цыфру:"))
print(numbers)
a="hello world"
print(a)

#2 задание делал с другом
a=int(input())
h=a//3600
m=(a//60)%60
s=a%60
if m<10:
    m=str('0'+m)
else:
    m=str(m)
if s<10:
    s=str('0'+s)
else:
    s=str(s)
print(str(h)+':'+str(m)+':'+str(s))

#задание 3
number=int(input("число:"))
temp = str(number)
n1 = temp + temp
n2 = temp + temp + temp
comp = number + int(n1) + int(n2)
print("Результат равен:", comp)

#4 задание я не понял что от меня требуется

#5 задание
vir=int(input(" выручка="))
prib=int(input(" прибыль="))
phin_rez=prib-vir
if phin_rez>0:
    print(prib/vir)
else:print(phin_rez)

# 6 Задание
a = int(input("значение:"))
b = int(input("значение:"))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(day)
