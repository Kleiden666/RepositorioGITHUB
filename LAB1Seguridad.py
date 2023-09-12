import requests
import json

def vigenere(texto, clave):
    resultado = ""
    clave = clave.upper()
    i = 0
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = clave[i % len(clave)]
            key_offset = ord(key_char) - 65
            resultado += chr(((ord(char) - offset + key_offset) % 26) + offset)
            i += 1
        else:
            resultado += char
    return resultado

def vigenere_decrypt(texto, clave):
    resultado = ""
    clave = clave.upper()  # Convierte la clave a mayúsculas
   
    i = 0

    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97  # Asegura que el offset sea correcto para mayúsculas o minúsculas
            key_char = clave[i % len(clave)]  # Obtiene el carácter de la clave correspondiente
            key_offset = ord(key_char) - 65  # Calcula el desplazamiento de la clave

            if char.isupper():
                decrypted_char = chr(((ord(char) - offset - key_offset) % 26) + offset)
            else:
                decrypted_char = chr(((ord(char) - offset - key_offset) % 26) + offset).lower()
            
            resultado += decrypted_char
            i += 1
        else:
            resultado += char
    
    return resultado

def rot_encrypt(texto, n):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97  # Determina el offset adecuado para mayúsculas o minúsculas
            resultado += chr(((ord(char) - offset + n) % 26) + offset)
        else:
            resultado += char
    return resultado

def rot_decrypt(texto, n):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97  
            resultado += chr(((ord(char) - offset - n) % 26) + offset)
        else:
            resultado += char
    return resultado

#Desafio 1


print("Desafio 1", "\n")

mensaje = "noPudimosHacerElDesafioDosPerdonSoloPrinteaSuper"
passwordVigerene = "cvqnoteshrwnszhhksorbqcoas"

mensajeRot15 = rot_encrypt(mensaje,15)
mensajevigerene = vigenere(mensajeRot15,"cvqnoteshrwnszhhksorbqcoas")
mensajeRot7 = rot_encrypt(mensajevigerene,7)
mensajeFinal = mensajeRot7

print("El mensaje cifrado es: ", mensajeFinal, "\n")


mensajePrincipalDes = mensajeFinal
mensajeMenos7 = rot_decrypt(mensajePrincipalDes,7)
mensajeVigereneDes = vigenere_decrypt(mensajeMenos7,"cvqnoteshrwnszhhksorbqcoas")
mensajeMenos15 = rot_decrypt(mensajeVigereneDes,15)

mensajeFinalDes = mensajeMenos15

print("El mensaje descifrado es: ",mensajeFinalDes,"\n")


headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"lfBdnxmcvUslsmHoJscncumNkgNvdmycScobHawiwhgGecbd"}'

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)

print("El mensaje descifrado es: ",response.text)

#####Desafio2

print("Desafio 2", "\n")

{"msg":"oemkd lyzqgvqxgptuuinqy nrkkfmnv"}

headers = {
    'Content-Type': 'text/plain',
}

responseDesafio2 = requests.get('http://finis.malba.cl/GetMsg', headers=headers)


print(responseDesafio2.text)

claveVigerene2 = "aobkqolrzsrigpknkufezioer"

mensajePagina = responseDesafio2.text

mensajeTraducido = json.loads((mensajePagina))

mensajeObtenido = mensajeTraducido["msg"]


mensajeDesafio2RotMenos7 = rot_decrypt(mensajeObtenido, 7)
mensajeVigereneDesafio2 = vigenere_decrypt(mensajeDesafio2RotMenos7,claveVigerene2)
mensajeDesafio2RotMenos15 = rot_decrypt(mensajeVigereneDesafio2,15)

mensajeFinalDesafio2 = mensajeDesafio2RotMenos15

print(mensajeFinalDesafio2)
