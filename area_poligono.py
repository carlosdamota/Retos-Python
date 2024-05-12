'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def area_poligono(poligono, lado1=None, lado2=None, lado3=None):
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


print(area_poligono("Cuadrado", 5))