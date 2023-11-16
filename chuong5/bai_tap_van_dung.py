#1.1
print("**  ** ******    **      **     *******")
print("**  ** **        **      **     **   **")
print("****** ******    **      **     **   **")
print("**  ** **        **      **     **   **")
print("**  ** ******    *****   *****  *******")
#1.2
x=10
y=5
tong = x+y
hieu = x-y
tich = x*y
thuong = x/y
print('Tổng của hai số    ', x, '+', y, '=',tong)
print('Hiệu của hai số    ', x, '-', y, '=',hieu)
print('Tích của hai số    ', x, '*', y, '=',tich)
print('Thương của hai số  ', x, '/', y, '=',thuong)
#1.3
ten_hang = "Sữa hộp Vinamilk"
so_luong = 5
gia = 25000
tien_can_tra = so_luong*gia
print("Tên hãng:", ten_hang)
print("Số lượng:",so_luong)
print("Tiền cần trả là:",tien_can_tra)
#1.4
import math
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác là:", s)
