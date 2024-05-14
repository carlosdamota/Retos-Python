'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

'''def area_poligono(poligono, lado1=None, lado2=None, lado3=None):
    if poligono == "Triangulo":
        area = (lado1 + lado2 + lado3)/2
        return area
    elif poligono == "Cuadrado":
        area = lado1 * lado1
        return area
    elif poligono == "Rectangulo":
        area = lado1 * lado2
        return area
    else:
        return "No es un poligono correcto" 

print(area_poligono(poligono, lado1, lado2, lado3))'''

def area_poligono(poligono, lado1=None, lado2=None, lado3=None):
    if poligono == "Triangulo":
        if lado1 is not None and lado2 is not None and lado3 is not None:
            semi_perimeter = (lado1 + lado2 + lado3) / 2
            area = (semi_perimeter * (semi_perimeter - lado1) * (semi_perimeter - lado2) * (semi_perimeter - lado3)) ** 0.5
            return area
        else:
            return "Debe proporcionar los tres lados del triángulo."
    elif poligono == "Cuadrado":
        if lado1 is not None:
            area = lado1 ** 2
            return area
        else:
            return "Debe proporcionar el lado del cuadrado."
    elif poligono == "Rectangulo":
        if lado1 is not None and lado2 is not None:
            area = lado1 * lado2
            return area
        else:
            return "Debe proporcionar ambos lados del rectángulo."
    else:
        return "No es un polígono válido."

poligono = input("Ingrese el tipo de polígono (Triangulo, Cuadrado o Rectangulo): ").capitalize()
if poligono in ["Triangulo", "Cuadrado", "Rectangulo"]:
    lado1 = float(input("Ingrese el primer lado: "))
    if poligono == "Triangulo":
        lado2 = float(input("Ingrese el segundo lado: "))
        lado3 = float(input("Ingrese el tercer lado: "))
    else:
        lado2, lado3 = None, None
else:
    lado1, lado2, lado3 = None, None, None

print(area_poligono(poligono, lado1, lado2, lado3))