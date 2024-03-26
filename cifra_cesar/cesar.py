from string import ascii_lowercase


def encripta(frase, rot=13):
    """Encripta o texto."""
    encriptado = ''
    for letra in frase.lower():
        if letra == ' ':
            encriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) + rot
            encriptado += ascii_lowercase[pos % 26]
    return encriptado


def decripta(frase, rot=13):
    """Decripta o texto."""
    decriptado = ''
    for letra in frase.lower():
        if letra == ' ':
            decriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) - rot
            decriptado += ascii_lowercase[pos % 26]
    return decriptado
