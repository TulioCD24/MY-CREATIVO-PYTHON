from collections import Counter

def contar_numeros_repetidos(cadena):
    # Filtrar los caracteres numéricos
    numeros = [int(caracter) for caracter in cadena if caracter.isdigit()]

    # Usar Counter para contar la frecuencia de cada número
    frecuencia_numeros = Counter(numeros)

    return frecuencia_numeros

# Ejemplo de uso TINKA
print("TINKA")
cadena_TINKA = "TK, 45, 9, 19, 26, 47, 25, 36, 8, 42, 25, 35, 29, 44, 7, 9, 27, 21, 11, 5, 22, 11, 17, 38, , 10, 42, 37, 2, 32, 1, 6, 40, 32, 17, 47, 24, 12, 14, 2, 15, 27, 18, 22, 8, 3, 1, 27, 19, 17, 3, 11, 18, 39, 12, 33, 8, 40, 24, 45, 41, 43, 25, 27, 34, 6, 7, 37, 19, 13, 26, 45, 2, 42, 19, 25, 38, 12, 37, 32, 42, 23, 2, 24, 27, 47, 25, 39, 35, 27, 6, 42, 38, 5, 33, 16, 12, 40, 27, 18, 44, 21, 39, 13, 17, 26, 24, 15, 39, 15, 38, 31, 9, 26, 43, 6, 38, 35, 23, 9, 31, 32, 48, 24, 44, 33, 25, 1, 13, 20, 42, 27, 23, 26, 38, 29, 21, 6, 11, 34, 28, 11, 1, 24, 5, 12, 43, 20, 10, 13, 22, 35, 43, 34, 14, 7, 38, 19, 26, 23, 25, 2, 11, 26, 1, 38, 13, 42, 30, 29, 13, 27, 21, 25, 11, 27, 2, 22, 9, 18, 41, 45, 44, 11, 35, 40, 27, 13, 8, 42, 41, 44, 36, 20, 43, 5, 38, 22, 16, 41, 28, 4, 10, 26, 18, 41, 6, 23, 45, 47, 19, 44, 42, 38, 4, 6, 31, 27, 24, 42, 34, 19, 47, 36, 5, 47, 46, 7, 8, 42, 28, 41, 48, 24, 19, 34, 41, 47, 7, 20, 3, 28, 29, 46, 27, 48, 6, 9, 24, 38, 33, 29, 46, 1, 33, 28, 25, 12, 44, 20, 22, 38, 28, 16, 14, 32, 43, 38, 25, 24, 11, 43, 25, 27, 34, 6, 7, 37, 19, 13, 26, 45, 2, 42, 19, 25, 38, 12, 37, 32, 42, 23, 2, 24, 27, 47, 25, 39, 35, 27, 6, 42, 38, 5, 33, 16, 12, 40, 21, 39, 13, 17, 26, 24, 15, 39, 15, 38, 31, 9, 26, 43, 6, 38, 35, 23, 9, 31, 32, 48, 24, 44, 33, 25, 1, 13, 20, 42, 27, 23, 26, 38, 29, 21, 6, 11, 34, 28, 11, 1, 24, 5, 12, 43, 20, 10, 13, 22, 35, 43, 34, 14, 7, 38, 19, 26, 23, 25, 2, 11, 26, 1, 38, 13, 42, 30, 29, 13, 27, 21, 25, 11, 27, 2, 22, 9, 18, 41"
resultado = contar_numeros_repetidos(cadena_TINKA)
print(resultado)

from collections import Counter

def contar_numeros_repetidos(cadena):
   # Filtrar solo los caracteres numéricos
    numeros = [int(caracter) for caracter in cadena if caracter.isdigit()]
    
    #Usar Counter para contar la  frecuencia de cada numero
    frecuencia_numeros = Counter(numeros)
    
    return frecuencia_numeros
     
#Ejemplo de uso numeros_Boliyapa
print("Boliyapa")
cadena_Boliyapa = "BY, 14, 44, 28, 47, 14, 30, 16, 23, 6, 7, 2, 25, 23, 7, 21, 16, 46, 4, 7, 26, 47, 16, 32, 47, 19, 42, 35, 32, 27, 31, 32, 35, 25, 9, 4, 30, 22, 34, 10, 2, 41, 45, 30, 31, 20, 3, 43, 40, 14, 20, 12, 34, 41, 6, 13, 26, 27, 33, 14, 11, 16, 8, 26, 36, 20, 31, 32, 35, 38, 25, 9, 4, 30, 22, 34, 10, 2, 41, 45, 30, 31, 20, 3, 43, 40, 14 "
resultado = contar_numeros_repetidos(cadena_Boliyapa)
print(resultado)

from collections import Counter

#Ejemplo de uso nuneros_SioSi
print("SioSi")
cadena_SioSi = " SS, 45, 32, 40, 41, 27, 46, 2, 26, 16, 3, 17, 7, 41, 16, 25,18, 39, 34, 24, 10, 18, 19, 9, 16, 42, 29, 25, 25, 44, 29, 11, 7, 5, 2, 16, 30, 1, 11, 35, 2, 1, 18, 32, 10, 22, 34, 14, 34, 15, 42, 34, 43, 8, 34, 6, 9, 35, 25, 33, 38, 1, 27, 45, 34, 9, 34, 30, 26, 32, 11, 29, 8, 13, 48, 7, 29, 30, 33, 16, 4, 47, 17, 10, 24, 10, 15, 44, 5, 42, 39, 44, 9, 32, 7, 19, 21, 40, 37, 14, 39, 29, 13, 26 "

resultado = contar_numeros_repetidos(cadena_SioSi)
print(resultado)
