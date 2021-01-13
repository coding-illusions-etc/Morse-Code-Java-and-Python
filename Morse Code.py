MORSE = {'A':'.-', 'B':'-...', 
        'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....', 
        'I':'..', 'J':'.---', 'K':'-.-', 
        'L':'.-..', 'M':'--', 'N':'-.', 
        'O':'---', 'P':'.--.', 'Q':'--.-', 
        'R':'.-.', 'S':'...', 'T':'-', 
        'U':'..-', 'V':'...-', 'W':'.--', 
        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
        '1':'.----', '2':'..---', '3':'...--', 
        '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', 
        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
        '?':'..--..', '/':'-..-.', '-':'-....-', 
        '(':'-.--.', ')':'-.--.-'}
##########################################################################################################################
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher = cipher + MORSE[letter] + ' '
        else: 
            cipher = cipher + ' '
    return cipher
###########################################################################################################################
def decrypt(message): 
    message = message + ' '
    decipher = '' 
    ctext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            ctext = ctext + letter 
        else: 
            i = i + 1
            if i == 2 : 
                decipher = decipher + ' '
            else:  
                decipher = decipher + list(MORSE.keys())[list(MORSE.values()).index(ctext)] 
                ctext = '' 
    return decipher
#############################################################################################################################
def main():
    val = raw_input("Enter 'En' to encrypt \nEnter 'De' to decrypt : \n")
    if(val == "En"):
        message = raw_input("Enter your message: ") 
        result = encrypt(message.upper()) 
        print (result)
    elif(val == "De"):
        message = raw_input("Enter your message: ")
        result = decrypt(message)  
        print (result)
    else:
        print("WRONG CHOICE")
if __name__ == '__main__': 
    main()
#############################################################################################################################
