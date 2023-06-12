#tALLER 1 PYTHON
#Oscar Alejandro Vargas Velilla
#FECHA: 11/06/2023


from datetime import date
hoy = date.today()                                                      
print ("La fecha de hoy es: ", hoy)
print ("Tu calculadora amiga esta aqui, ingrese los datos que le pedimos a continuacion")
n1=int (input("Ingrese el primer número: "))
n2=int (input("Ingrese el segundo número: ")) 

suma = n1+n2
resta = n1-n2
division = n1/n2
producto = n1*n2
dibujo = '''
                       __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\    .-"       `--""-.__.'=====================-,
    \ '-'`        .___.--._)=========================|
     \            .'      |                          |
      |     /,_.-'        |        TUS               |
    _/   _.'(             |    RESULTADOS            |
   /  ,-' \  \            |        ESTAN ABAJO       |
   \  \    `-'            |                          |
    `-'                   '--------------------------'
'''

print(dibujo)


print("/n")
print ()
print("_______________________________________________________________________")
print("| La suma entre:      |",n1,"+",n2,"|es igual a= |",suma,"","",) 
print("| La resta entre:     |",n1,"-",n2,"|es igual a= |",resta,"","",) 
print("| La división entre:  |",n1,"/",n2,"|es igual a= |",division,"",) 
print("| El producto entre:  |",n1,"*",n2,"|es igual a= |",producto,)
print("________________________________________________________________________")
