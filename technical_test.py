import sys
def odd_number(angka):
    list_kosong = []
    list_kosong = [angka for angka in range(0, angka+1) if angka % 2 == 1]
    list_kosong.reverse()
    return list_kosong

def only_vowels(kata):
    vowels = [x for x in kata if x in '[[aeiouAEIOU]]']
    vowels = ''.join(vowels)    
    return vowels
    
if __name__ == "__main__":
    while True:
        soal = input("Which question (1, 2 or type q to exit) ? ")
        if soal == "1":
            angka = int(input("Please input your number: "))
            if angka > 0:
                print("-" * 90)
                print(f'Reversed odd numbers: {odd_number(angka)}')
                print("-" * 90)
            else:
                print("-" * 90)
                print("Error")
                
        elif soal == "2":    
            kata = input("Please input your words: ")
            if only_vowels(kata) == "":
                print("-" * 90)
                print('''Your input doesn't contain vowels''')
                print("-" * 90)
            else:
                print("-" * 90)
                print(f'The vowels inside `{kata}` words is: {only_vowels(kata)}')
                print("-" * 90)
        elif soal == "q":
            sys.exit("Thank You!")
        else:
            print("Sorry, that was invalid number")
