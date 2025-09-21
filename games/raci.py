import random
import main

def start():
    while True:
        bentuk_goa = '|_|'
        goa_kosong = [bentuk_goa] * 4

        raci_position = random.randint(1, 4)

        goa = goa_kosong.copy()
        goa[raci_position - 1] = '|0_0|'

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(f'Coba perhatikan goa dibawah ini\n{goa_kosong}\n')

        pilihan_user = int(input('Menurut kamu di goa nomor berapa RACI berada? [1, 2, 3, 4]: '))

        if pilihan_user == raci_position:
            print(f'{goa} \n Selamat kamu benar! RACI berada di goa nomor {raci_position} dan pilihan kamu {pilihan_user}.')
        else:
            print(f'{goa} \n Sayang sekalis, kamu kurang beruntung. RACI berada di goa nomor {raci_position} dan pilihan kamu {pilihan_user}.')

        play_again = input('\nApakah kamu ingin bermain lagi? [y/n]: ')
        if play_again == 'n':
            main.menu()

if __name__ == '__main__':
    start()