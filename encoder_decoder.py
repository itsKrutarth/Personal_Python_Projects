

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def shiftChar(type, shift, char):
    if type=='e':
        index = alphabet.index(char)
        position = index+shift
        if position>len(alphabet)-1:
            char = alphabet[position-25]
        else:
            char = alphabet[position]
        return char
    elif type=='d':
        index = alphabet.index(char)
        position = index - shift
        if position < 0:
            char = alphabet[position - 1]
        else:
            char = alphabet[position]
        return char

def encrypt(type, text, shift):
    if(shift>0):
        newStr = ""
        for char in text:
            if char.isalpha():
                char = shiftChar(type, shift,char)
            newStr+=char
        return newStr


def decode(type, text, shift):
    if(shift>0):
        newStr=("")
        for char in text:
            if char.isalpha():
                char = shiftChar(type,shift,char)
            newStr+=char
        return newStr

if(direction=='encode'):
    print(f"encrypted text: {encrypt('e', text, shift)}")
elif(direction=="decode"):
    print(f"decoded text: {decode('d',text, shift)}")


