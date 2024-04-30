import random

welcome_message = "WELCOME TO DAVIPY GAMES"
davipy_position = random.randint(1, 4)
yrn = "n" 
#yrn (yes or no for user choice input)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama kamu: ")
print(f'''
halo {nama_user}! Coba perhatikan KOTAK dibawah ini
[]  []  []  []
''')

pilihan_user = int(input("menurutmu di kotak apa DAVIPY berada? [ 1 / 2 / 3 / 4 ]: "))
user_choice = input(f"apakah kamu Yakin dengan pilianmu? y/{yrn}: ")

if user_choice == yrn:
    print("oke, terimakasih sudah menggunakan program ini:)")
    exit()
elif pilihan_user == davipy_position:
    print(f"selamat {nama_user}, kamu menang! Davipy berada di dalam kotak nomor {davipy_position} dan pilihanmu adalah kotak nomor {pilihan_user}")   
else :
    print(f"kamu kalah! Davipy bukan berada di kotak {pilihan_user}. tetapi ada di dalam kotak {davipy_position}")