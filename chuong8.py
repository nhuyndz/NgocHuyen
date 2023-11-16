#8.1
print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=eval(input("Nhập số a:"))
b=eval(input("Nhập số b:"))
c=eval(input("Nhập số c:"))
d=eval(input("Nhập số d:"))
n=0
h=0
while(n<a)or(n<b)or(n<c)or(n<d):
    n+=1
h=n
while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
print("max =",n)
print("min =",h)

#8.2
a=eval(input("Nhập số:"))
print("Giá trị tuyệt đối của",a,"là:","|",a,"|=",abs(a))

#8.3
print("Giải phương trình ax+b=0")
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else: print("Phương trình vô nghiệm.") 
else: 
    print('Nghiệm của phương trình là: x = ', -b/a)

#8.4
a = eval(input("nhap do dai canh a: "))
b = eval(input("nhap do dai canh b: "))
c = eval(input("nhap do dai canh c: "))
if a+b<c and b+c<b:
    print("day khong phai la tam giac")
else:
    print("day la mot tam giac")
    import math
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)

#8.5
a = int(input("Nhập năm: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("năm", a, "là năm nhuận")
else:
    print("năm", a, "không phải là năm nhuận")

#8.6
def tinh_tien_di_chuyen(so_km, loai_xe):
    if loai_xe == 4:
        if so_km <= 0.8:
            return 0.8 * 11000
        elif so_km <= 20:
            return 0.8 * 11000 + (20 - so_km) * 12100
        else:
            return 0.8 * 11000 + (20 - 0.8) * 12100 + (so_km - 20) * 10000
    elif loai_xe == 7:
        if so_km <= 0.8:
            return 0.8 * 13000
        elif so_km <= 30:
            return 0.8 * 13000 + (30 - so_km) * 14100
        else:
            return 0.8 * 13000 + (30 - 0.8) * 14100 + (so_km - 30) * 12000
loai_xe = int(input("Cho biết loại xe là 4 chỗ hay 7 chỗ ?"))
so_km = float(input("Nhập số km chạy = "))
time_cho = float(input("Thời gian chờ (phút chờ) = "))
tien_cho = (time_cho - 5) * 0.8 if time_cho >= 5 else 0
tien_di_chuyen = tinh_tien_di_chuyen(so_km, loai_xe)
tien_cuoc = tien_cho + tien_di_chuyen
print(f"Cước phí xe taxi {loai_xe} chỗ của quý khách là {tien_cuoc:.2f}")

#8.7
a=eval(input("Nhập số KWh tiêu thụ:"))
if a>=0:
    if a<=50:
       print("Tổng số tiền phải trả là:",a*1678,"đồng.")
    elif a<=100:
       print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
    elif a<=200:
       print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
    elif a<=300:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
    elif a<=400:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
    else:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
else:
   print("Số KWh không hợp lệ.")

#8.8
print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")

a = int(input("Nhập mã loại phòng:"))
b = int(input("Nhập số đêm:"))

if a == 1:
    c = 1260000
elif a == 2:
    c = 1550000
elif a == 3 or a == 4:
    c = 1830000
elif a == 5 or a == 6:
    c = 2120000
elif a == 7:
    c = 2540000
elif a == 8:
    c = 4800000
else:
    print("Vui lòng chọn lại mã loại phòng.")
    c = 0
if c != 0:
    if b == 1:
        print("Giá tiền phải trả là:", c, "đồng.")
    elif b in [2, 3]:
        print("Giá tiền phải trả là:", c * b * 0.75, "đồng.")
    elif b >= 4:
        print("Giá tiền phải trả là:", c * b * 0.7, "đồng.")
    else:
        print("Vui lòng nhập lại số đêm.")
 
 #8.9
a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)

#8.10
n = int(input("Nhập n: \n"))
x = int(input("Nhập x: \n"))
S = (x*x + 1)**n 
print ("S = (x*x + 1)^n =",S)

#8.11
n = int(input("Nhập n: \n"))
x = int(input("Nhập x: \n"))
A= (x*x + x + 1)**n + (x*x - x + 1)**n
print ("A= (x*x + x + 1)**n + x*x - x + 1)**n =",A)

#8.12
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!")

#8.13
# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các cố nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu
import math
n = int(input("nhập số N: "))
def A(n):
    j = []
    a = 0
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
A(n)
B(n)
C(n)
D(n)
E(n)
F(n)

#8.14
def tinh_tong(n):
    tong = 0
    for i in range(n):
        so = int(input("Nhập số thứ {}: ".format(i+1)))
        tong += so
    return tong

n = int(input("Nhập số lượng số nguyên: "))
print("Tổng của {} số nguyên là: {}".format(n, tinh_tong(n)))

#8.15
print("Chương trình tính tổng N số nguyên")
tong = 0
while True: 
    so = int(input("Nhập một số nguyên (kết thức là số 0): "))
    if so == 0:
        break
    tong += so
print("S =",tong)

#8.16
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b) 

#8.17
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = a*b
for i in range (b, c+1):
    if i%a == 0 and i%b == 0:
        d = i
        break
print("UCNN của", a, "và", b, "là:", i)

#8.18
def so_hoan_hao(n):
    tong_uoc_so = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc_so += i
    return tong_uoc_so == n

x = int(input("Nhập vào một số: "))
if so_hoan_hao(x):
    print(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo.")

#8.19
def day_so(n):
    numbers = list(range(1, n + 1))
    numbers.reverse()
    for number in numbers:
        if number % 2 != 0:
            print(number)
day_so(10)

#8.20
def e_mu_x(x, sai_so, n=0, ket_qua=1):
    if abs(x**n / factorial(n)) < sai_so or n > 100:
        return ket_qua
    else:
        n += 1
        ket_qua += x**n / factorial(n)
        return e_mu_x(x, sai_so, n, ket_qua)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
x = float(input("Nhập giá trị của x: "))
sai_so = 1e-4
ket_qua = e_mu_x(x, sai_so)
print(f"e^{x} gần đúng với sai số {sai_so} là: {ket_qua}")

