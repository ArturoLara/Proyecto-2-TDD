def Text_Data_Miner(texto, path_stop_words="stop_words.txt"):

    if type(texto) is not str or type(path_stop_words) is not str:
        raise TypeError

    signos_puntuacion = [",", ".", ";", ":", "?", "¿", "!", "¡", "(", ")", "[", "]", "_", "-", "\"", "/", "*", "'", "´",
                         "`", "+", "¨"]

    for puntuacion in signos_puntuacion:
        texto = texto.replace(puntuacion, " ")

    #Se codifica a unicode y se decodifica a UTF-8
    texto.encode().decode()
    palabras = texto.split()

    for i in range(len(palabras)):
        palabras[i] = palabras[i].lower()

    with open(path_stop_words, encoding="utf8") as stops:
        stop_words = stops.readline().split()
        stops.close()

    for stops in stop_words:
        while stops in palabras:
            palabras.remove(stops)

    diccionario_repetidos = {}
    for palabra in palabras:
        if palabra in diccionario_repetidos.keys():
            diccionario_repetidos[palabra] += 1
        else:
            diccionario_repetidos[palabra] = 1

    lista_palabras_repetidas = []
    for key in diccionario_repetidos.keys():
        lista_palabras_repetidas.append([key, diccionario_repetidos[key]])

    return sorted(lista_palabras_repetidas, key=lambda tup: tup[1], reverse=True)

