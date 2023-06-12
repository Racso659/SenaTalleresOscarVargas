from datetime import date 
hoy = date.today() 
print("La fecha de hoy es :",hoy) 
nombre = str(input("Digite su nombre: ")) 
print("Hola",nombre,) 
dibujo = '''
                       __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\    .-"       `--""-.__.'=====================-,
    \ '-'`        .___.--._)=========================|
     \            .'      |                          |
      |     /,_.-'        |                          |
    _/   _.'(             |    ¡¡¡BIENVENIDO!!!      |
   /  ,-' \  \            |                          |
   \  \    `-'            |                          |
    `-'                   '--------------------------'
'''
print(dibujo)

a = int(input("Digite el primer número: ")) 
b = int(input("Digite el segundo número: ")) 
c = int(input("Digite el tercer número: "))  
x = [a , b, c]  

print("El valor maximo de x es: ",max(x)) 
print("El valor minimo de x es: ",min(x)) 
print("La suma de los 3 valores es: ",sum(x)) 
print()  
z = float(input("Digite un número con decimales : ")) 
redondo = round(z) 

print("El valor de: ",z,"redondeado es: ",redondo) 
print()  
frase = input("Digite una oracion: ") 
print("La frase en mayuscula es: ",frase.upper()) 
print("La frase en minuscula es: ",frase.lower()) 
print("La frase con mayuscula incial es: ",frase.capitalize()) 
print("La frase con palabras en mayusculas es: ",frase.title()) 
print("La longitud de la frase es: ",len(frase),"caracteres") 
print() 

print("FIN")