

encryption chiper text

def casear_de(messege,shift,mode='encrpt'):
    result=""
    for char in messege:
        
        shift_base = 65 if char.isupper() else 97
        shift_value = shift if mode == 'encrpt' else -shift
        result+=chr((ord(char)-shift_base+shift_value)%26+shift_base)

    else:
        result+=char

    return result

messege = input("Enter the password: ")
shift = int(input("Enter the value: "))
encryption = casear_de(messege,shift,mode='encrpt')
print(f"Encrypt messege:{encryption}")
decryption = casear_de(messege,shift,mode='decrpt')
print(f"decrypt messege:{decryption}")
