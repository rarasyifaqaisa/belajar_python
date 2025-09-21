from libs import welcome_message, exit_program
from games import raci
from tools import toko

def menu():
    user_option = int(input(f'Menu program:\n1. Game RACI\n2. Toko\n3. Keluar\nPilih menu yang ingin dijalankan [1/2]: '))

    if user_option == 1:
        raci.start()
    elif user_option == 2:
        toko.start()
    elif user_option == 3:
        exit_program()
    else:
        print('Pilihan tidak valid!')

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()