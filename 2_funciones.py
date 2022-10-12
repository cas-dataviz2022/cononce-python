def miFuncion():
    """
    La importancia de la alineación del código.
    Esto es llamado IDENTACIÓN.

    Este espacio es útil para 'documentar' la función/método.
    """

    suma10 = 1 + 9
    producto12 = 2 * 6
    verdadero = True
    falso = False
    nulo = None
    flotante = f"Un número Flotante o con decimales es: {float(50/2)}"

    saludo = """
    Hola,
    Este es un mensaje de múltiples líneas
    """
    retorno = saludo + ("*" * 10) + """
    producto 12 = {producto}
    suma 10 = {suma}
    verdadero es: {verdad}
    falso es: {negativo}
    nulo es: {nulo}
    {flotante}
    """.format(
        producto=producto12,
        suma=suma10,
        verdad=verdadero,
        negativo=falso,
        nulo=nulo,
        flotante=flotante
    )

    return retorno

# Comentario de Ejemplo

valor = miFuncion()

print(valor)