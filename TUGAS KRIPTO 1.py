text = str(input("Enter the text: "))

ascii_values = [ord(char) for char in text]


kunci = str(input("Enter the key: "))
listkunci = [char for char in kunci]
asciiKey = [((ord(char))-97) for char in kunci]



print("output:")
for idx,val in enumerate(asciiKey):
    for index,value in enumerate(ascii_values):

        ascii_values[index] = ascii_values[index]+val
        if ascii_values[index] > 122:
            ascii_values[index] = ascii_values[index]- 26
        characters = [chr(value) for value in ascii_values]
        hasil=  ""
        for x in characters:
            hasil = hasil+x
    print("karakter ke-",idx+1, " ", hasil," (",listkunci[idx],")")
            

print("ciphertext:", hasil)
