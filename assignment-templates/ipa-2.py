'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_index = (alphabet.index(letter) + shift) % len(alphabet)
    shift_letter = alphabet[shift_index]

    return shift_letter

print(shift_letter("A", 0))
print(shift_letter("A", 2))
print(shift_letter("Z", 1))
print(shift_letter("X", 5))
print(shift_letter(" ", 3))

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar_cipher = ""

    for character in message:
        if character.isalpha():
            is_uppercase = character.isupper()
            character_index = alphabet.index(character.upper())
            shifted_index = (character_index + shift) % 26
            shifted_character = alphabet[shifted_index]

            if not is_uppercase:
                shifted_character = shifted_character.lower()
        else:
            shifted_character = character

        caesar_cipher += shifted_character

    return caesar_cipher

print(caesar_cipher("HELLO", 3))
print(caesar_cipher("WORLD", 1))
print(caesar_cipher("PYTHON", 5))
print(caesar_cipher("A B C", 2))

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_amount = alphabet.index(letter_shift.upper())
    shift_index = (alphabet.index(letter.upper()) + shift_amount) % 26
    shift_by_letter = alphabet[shift_index]

    if letter.islower():
        shift_by_letter = shift_by_letter.lower()

    return shift_by_letter

print(shift_by_letter("A", "A"))
print(shift_by_letter("Z", "C"))
print(shift_by_letter("B", "H"))
print(shift_by_letter(" ", "_"))

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_extended = key * ((len(message) // len(key)) + 1)
    vigenere_cipher = ""

    for i, char in enumerate(message):
        if char == " ":
            vigenere_cipher += " "
        else:
            message_index = alphabet.index(char)
            key_index = alphabet.index(key_extended[i])
            shift_index = (message_index + key_index) % 26
            vigenere_cipher += alphabet[shift_index]

    return vigenere_cipher

print(vigenere_cipher("A C", "KEY"))
print(vigenere_cipher("LONGTEXT", "KEY"))
print(vigenere_cipher("HELLO WORLD", "ABC"))

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(message) % shift != 0:
        message += '_' * (shift - (len(message) % shift))

    scytale_cipher = ''.join(
        message[(i // shift) + (len(message) // shift) * (i % shift)]
        for i in range(len(message))
    )

    return scytale_cipher

print(scytale_cipher("INFORMATION_AGE", 3))
print(scytale_cipher("INFORMATION_AGE", 4))
print(scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8))

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    num_rows = len(message) // shift
    num_cols = shift

    grid = [message[i:i+num_cols] for i in range(0, len(message), num_cols)]

    scytale_decipher = ''
    for col in range(num_cols):
        for row in range(num_rows):
            scytale_decipher += grid[row][col]

    return scytale_decipher

print(scytale_decipher("IMNNA_FTAOIGROE", 3))
print(scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8))
print(scytale_decipher("IRIANMOGFANEOT__", 4))
