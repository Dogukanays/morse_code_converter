morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--', ':': '---...',
              '/': '-..-.', '&': '.-...', '(': '-.--.', ')': '-.--.-', '!': '-.-.--', "'": '.----.', '"': '.-..-.',
              '?': '..--..', '=': '-...-', '+': '.-.-.', " ": "/"}

converter_on = True
while converter_on:

    user_message = input("Type your message: ").lower()

    if user_message == "off":
        converter_on = False

    else:
        response = ""
        for char in user_message:
            if char not in morse_code:
                print("Invalid character!")
                response = ""
                break
            else:
                response += morse_code[char]
            response += " "
        print(response)
