# GLOBAL DICT
morse_dict = {
    'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
    'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--',
    'z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
}
# PROGRAM
def main():
    while True:  
        word = input('Word to transalte: ').lower()
        morse_word = to_morse(word)
        print(morse_word)
        if input("Do You want to transalte another word ? y/n\n").lower() == 'n':
            break
# FUNCTIONS
def to_morse(word):
    return ''.join([morse_dict.get(letter,' ') for letter in word])

# RUN
if __name__ == '__main__':
    main()