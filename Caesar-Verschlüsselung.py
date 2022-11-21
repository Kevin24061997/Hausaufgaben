zeichen = 'A'
zahl = ord('A')
print('ord: ', zeichen, '->', zahl)
zahl = 90
zeichen = chr(zahl)
print('chr: ', zahl, '->', zeichen)

zeichen = 'P'
schluessel = 7
zahl = ord(zeichen)
neueZahl = zahl + schluessel
neuesZeichen = chr(neueZahl)
print(neuesZeichen)

#Funktionsdefinition
# def verschiebung(zeichen, schluessel):
#     zahl = ord(zeichen)
#     range = 90 - zahl
#     if schluessel - range > 0:
#         zahl = 64
#         schluessel = schluessel - range
#     neueZahl = zahl + schluessel 
#     neuesZeichen = chr(neueZahl)
#     return neuesZeichen

def verschiebungGrossKlein(zeichen, schluessel):
    result = ""
    if (zeichen.isupper()):
         result += chr((ord(zeichen) + schluessel-65) % 26 + 65)
    else:
         result += chr((ord(zeichen) + schluessel - 97) % 26 + 97)
    return result

def verschiebungzurueckGrossKlein(zeichen, schluessel):
    result = ""
    if (zeichen.isupper()):
         result += chr((ord(zeichen) - schluessel-65) % 26 + 65)
    else:
         result += chr((ord(zeichen) - schluessel - 97) % 26 + 97)
    return result

def verschlüsselung(text, schluessel):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += verschiebungGrossKlein(char, schluessel)
    return result

def entschluesseln(text, schluessel):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += verschiebungzurueckGrossKlein(char, schluessel)
    return result


# Funktionsaufrufe
text = input("Ein Wort eingeben: ")
text = str(text)
schluessel = input("Geben Sie einen Schlüssel ein: ")
schluessel = int(schluessel)

encryptedText = verschlüsselung(text, schluessel)
print(encryptedText)
decryptedText = entschluesseln(encryptedText, schluessel)
print(decryptedText)