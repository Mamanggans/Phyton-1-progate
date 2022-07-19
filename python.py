#latihan 3 

# Cetak 7 sebagai sebuah integer
print(7)

# Cetak penjumlahan dari 9 dan 3
print (9+3)

# Cetak '9 + 3' sebagai string
print ("9+3")


# latihan 4

# Cetak hasil dari 9 / 2
 print(9/2)

# Cetak hasil dar 7 * 5
print(7*5)

# Cetak sisa dari 5 dibagi 2 menggunakan %
print(5%2)

# latihan 5

# Tetapkan 'Bob' ke variable name
name = 'bob'

# Cetak nilai dari variable name
print(name)

# Tetapkan 7 ke variable number
number = 7

# Cetak nilai dari variable number
print(number)


# latihan 6 

apple_price = 2
apple_count = 8

# Berikan hasil dari apple_price * apple_count ke variable total_price 
total_price = apple_price * apple_count

# Cetak nilai dari variable total_price 

print(total_price)

#latihan 7 

money = 20
print(money)

# Tambahkan 50 ke variable money
money = money + 50

# Cetak nilai dari variable money
print(money)

#latihan 8 
# Tetapkan 'Bob' ke variable my_name 
my_name = "Bob"

# Cetak 'Nama saya Bob' dengan menggabungkan variable my_name dan sebuah string
print('Nama saya' + name)

#latihan 9 
age = 24
# Cetak 'Saya berusia 24 tahun' menggunakan variable age
print("Saya berusia" + str(age) + " tahun")

count = '5'
# Ubah variable count ke tipe data integer, tambahkan 1, dan cetak hasilnya
count = int(count) + 1

print(count)

#latihan 9 statement IF 

x = 7 * 10
y = 5 * 6

# Jika x sama dengan 70, cetak 'x adalah 70'
if x == 70:
  print("x adalah 70")


# Jika y tidak sama dengan 40, cetak 'y bukan 40' 
if y != 40:
  print("y bukan 40")

#latihan 10 statement if
x = 10
# Jika x lebih besar dari 30, cetak 'x lebih besar dari 30'
if x > 30:
  print("x lebih besar dari 30")


money = 5
apple_price = 2
# Jika money sama dengan atau lebih besar dari apple_price, cetak 'Anda dapat membeli apel'
if money >= apple_price:
  print ("Anda dapat membeli apel")


# latihan 11 else if 

money = 2
apple_price = 2

if money > apple_price:
    print('Anda dapat membeli apel')
# Ketika kedua variable memiliki nilai yang sama, cetak 'Anda dapat membeli apel tetapi dompet Anda akan menjadi kosong'
elif money == apple_price:
    print("Anda dapat membeli apel tetapi dompet Anda akan menjadi kosong")

else:
    print('Uang Anda tidak mencukupi')
 
 
 # latihan 12 AND OR dan NOT 
x = 20
# Jika x berkisar antara 10 dan 30 (inklusif), cetak 'x berkisar antara 10 dan 30'
if x >= 10 and x <= 30:
    print("x berkisar antara 10 dan 30")


y = 60
# Jika y lebih kecil dari 10 atau lebih besar dari 30, cetak 'y lebih kecil dari 10 atau lebih besar dari 30'
if y < 10 or y > 30:
    print("y lebih kecil dari 10 atau lebih besar dari 30")


z = 55
# Jika z tidak sama dengan 77, print 'z bukan 77'
if not z == 77:
    print("z bukan 77")

# latihan 13 menghitung harga belanjaan 

# Berikan 2 ke variable apple_price 
apple_price = 2


# Berikan 5 ke variable count 
count = 5

# Berikan hasil dari apple_price * count ke variable total_price 
total_price = apple_price * count

# Dengan menggunakan variable count, cetak 'Anda akan membeli .. apel' ubah dulu ke string dengan str()
print("Anda akan membeli"+str(count)+"apel")

# Dengan menggunakan variable total_price, cetak 'Harga total adalah .. dolar' ubah dulu ke string dengan str()
print("Harga total adalah"+str(total_price)+"dolar")

#latihan 14 input 
apple_price = 2

# Terima jumlah apel dengan menggunakan input(), dan berikan hasilnya ke variable input_count 
input_count = input("Mau berapa apel? :")

# Ubah variable input_count ke integer, dan berikan hasilnya ke variable count 
count = int(input_count) #ubah dulu ke interger agar bisa dihitung 
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

# latihan akhir 
apple_price = 2
# Berikan 10 ke variable money 
money = 10

input_count = input('Mau berapa apel?: ')
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

# Tambahkan control flow berdasarkan perbandingan antara money dan total_price
if money > total_price:
    print("Anda telah membeli"+ str(count) +"apel")
    print("Uang Anda tinggal" +str(money - apple_price)+"dolar")
elif money == total_price:
    print("Anda telah membeli"+ str(count) +"apel")
    print("Dompet Anda kosong")
else:
    print("Uang Anda tidak mencukupi")
    print("Anda tidak dapat membeli apel sebanyak itu")