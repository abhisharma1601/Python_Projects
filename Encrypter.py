main_string="abcdefghijklmnopqrstuvwxyz "
key_string="QWERTYUIOPLKJHGFDSAZXCVBNM@"

def encode_text():
    output = ''
    input_text=input("enter text:\n")
    for i in input_text:
        pos = main_string.find(i)
        char = key_string[pos]
        output = output + char
    return output

def decode_text():
    output=""
    input_text=input("enter text:\n")
    for i in input_text:
        pos = key_string.find(i)
        char = main_string[pos]
        output = output + char
    return output

while True:
    print("1.Encode \t\t2.Decode\t\t3.quit")
    input_user = input("enter accordingly:\n")
    if input_user == "1":
        print(encode_text())
    elif input_user == "2":
        print(decode_text())
    elif input_user == "3":
        print("thank you for using")
        break