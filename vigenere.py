#possible characters
characters="abcdefghijklmnopqrstuvwxyz"
characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters += "1234567890"
characters += " !@#$%^&*()-_+=`~;:'[]{}|<>,./?"
characters += "\"\\"


#available characters
character_count = len(characters)

#supported characters
print("supported characters:\n" + characters + "\n")

#encryption
def encrypt_character(plain, key):
    #plain char & key char into number codes
    key_code = characters.index(key)
    plain_code = characters.index(plain)

    #plain + key and loop back to zero at character_count
    cipher_code = (key_code + plain_code) % character_count

    #cipher_code back to character
    cipher = characters[cipher_code]

    #return ciphertext character
    return cipher

def encrypt(plain, key):
    #empty string to fill with ciphertext
    cipher = ""

    #loop over every character in plaintext
    for (plain_index, plain_character) in enumerate(plain):

        #using index of plain character to get corresponding key character
        key_index = plain_index % len(key) 
        key_character = key[key_index]

        #encrypt plain character with key character
        cipher_character = encrypt_character(plain_character, key_character)

        #add new cipher character to ciphertext
        cipher +=  cipher_character

    #return full ciphertext
    return cipher

#decryption
def invert_character(character):
    #character back into number code
    character_code = characters.index(character)

    #get opposite character
    inverted_code = (character_count - character_code) % character_count
    inverted_character = characters[inverted_code]

    return inverted_character

def invert(text):
    #empty string to fill with inverted text
    inverted_text = ""

    #loop over every character in text,invert it, add to inverted text
    for character in text:
        inverted_text += invert_character(character)

    return inverted_text

while True:
    plaintext = input("Message: ")
    keytext = input("Password: ")

    #whether the msg is already encrypted
    encrypted = plaintext.startswith("!")

    #if encrypted, remove the first character from plain text (!), invert key
    if encrypted:
        plaintext = plaintext[1:]
        keytext = invert(keytext)

    ciphertext = encrypt(plaintext, keytext)

    #if not encrypted, stick ! in the beginning to know its already encrypted
    if not encrypted:
        ciphertext = "!" + ciphertext

    print("Output: " + ciphertext)
    print()

    
print("message: " + plaintext)
print("password: " + keytext)
print("output: " + ciphertext)

