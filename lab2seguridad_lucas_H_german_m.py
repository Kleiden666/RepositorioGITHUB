import hashlib
import codecs

def encriptadoVigenere(mensaje, clave, caracteres):
    mensaje_encriptado = ''
    c = 0

    for i in mensaje:
        if i.upper() in caracteres:
            clave_letra = clave[c % len(clave)].upper()
            c += 1

            shift = caracteres.index(clave_letra)
            letraEncriptada = caracteres[(caracteres.index(i.upper()) + shift) % len(caracteres)]
            mensaje_encriptado += letraEncriptada

        else:
            mensaje_encriptado += i

    return mensaje_encriptado

def decriptadoVigenere(mensaje_encriptado, clave, caracteres):
    mensaje_desencriptado = ''
    c = 0

    for i in mensaje_encriptado:
        if i.upper() in caracteres:
            clave_letra = clave[c % len(clave)].upper()
            c += 1

            shift = -caracteres.index(clave_letra)
            letraDesencriptada = caracteres[(caracteres.index(i.upper()) + shift) % len(caracteres)]
            mensaje_desencriptado += letraDesencriptada

        else:
            mensaje_desencriptado += i

    return mensaje_desencriptado

def rot_encrypt(texto, n):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            offset = 65 if letra.isupper() else 97  # Determina el offset adecuado para mayúsculas o minúsculas
            resultado += chr(((ord(letra) - offset + n) % 26) + offset)
        else:
            resultado += letra
    return resultado

def rot_decrypt(texto, n):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            offset = 65 if letra.isupper() else 97  # Determina el offset adecuado para mayúsculas o minúsculas
            resultado += chr(((ord(letra) - offset - n) % 26) + offset)
        else:
            resultado += letra
    return resultado
#abriMensaje

#desarrollo
#creamos un txt y se gurada el mensaje ingresado
Texto_mensaje = open('mensaje.txt','w')

mensajeEntrante = input("ingrese su mensaje: ")

mensaje = mensajeEntrante.upper()

Texto_mensaje.write(mensaje)

Texto_mensaje.close()
#se cierra el mensaje ingresado


claveVigerene ='WAOSEFXHIJKLMFDPQRSTIIIYZ'
clave = "sus"



#encriptado


Texto_mensaje = open('mensaje.txt','r')
Texto_Oculto = open('Texto_Oculto.txt','w')


Entrada = Texto_mensaje.read()


mensajeRot13 = rot_encrypt(Entrada,13)
mensajeVigenere = encriptadoVigenere(mensajeRot13,clave,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
mensajeFinal = mensajeVigenere

Texto_Oculto.write(mensajeFinal)
Texto_Oculto.close() #Mensaje cifrado y guardado en txt


#desencriptado

Texto_Oculto = open('Texto_Oculto.txt','r') #se vuelve a abrir para extraer el mensaje

Entrada_oculta = Texto_Oculto.read()

nuevoMensajeVigenere = decriptadoVigenere(Entrada_oculta,clave,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nuevoRot13 = rot_decrypt(nuevoMensajeVigenere,13)
mensajeNuevoFinal = nuevoRot13
Texto_Oculto.close()

#Aplicacion hash



hashObjeto = hashlib.sha256(Entrada.encode())
hashValor1 = hashObjeto.hexdigest()

hashObjeto2 = hashlib.sha256(mensajeNuevoFinal.encode())
hashValor2 = hashObjeto2.hexdigest()

#print
print(Entrada_oculta)#encriptado rot y vigenere
print(mensajeNuevoFinal)#desencriptado
print(hashValor1)#hash al mensaje 
print(hashValor2)#hash con rot y vigenere

if  hashValor1 ==  hashValor2 :
    print("Ambas salidas coinciden")

