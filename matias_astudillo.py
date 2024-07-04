from os import system
system("cls")

'''
La distribuidora de agua purificada “CleanWasser”, necesita desarrollar un sistema que permita registrar los pedidos para enviar la hoja
de ruta al repartidor. Para el funcionamiento del sistema se requiere las siguientes funcionalidades:
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa

-registrar pedido:
Para registrar un pedido se requiere lo siguiente: 
Nombre y apellido del cliente, comuna, detalle del pedido. 
Por ejemplo, la empresa vende
dispensadores de 6, 10 y 20 litros. Debe permitir ingresar la cantidad de cada cilindro a solicitar y considerar que la suma de las cantidades
(de cada cilindro) deben sumar más de cero (para que tenga sentido el pedido).
Por lo tanto, un detalle de pedido podría verse registrado de la siguiente manera
ID pedido   Cliente     Direccion       Sector      Disp. 6lts      Disp. 10lts      Disp. 20lts
321321      Matias Astudillo   duqueco   Duqueco     1              1                0
'''
pedidos=[]
pedido=[]
sectores=["Concepcion","Chiguayante","Talcahuano","Hualpen","San Pedro"]
def registrar_pedido():
    #el id del pedido debe ser random
    id= 321321
    print(id)
    while True:
        cliente= input("ingrese nombre y apellido del cliente: ")
        if len(cliente)<3 and cliente.isalnum:
            print("ingrese nuevamente y separe apellido por un espacio")
        else:
            print(f"cliente: {cliente}")
            break
    while True:
        direccion= input("ingrese direccion del pedido: ")
        if len(direccion)<10:
            print("ingrese nuevamente")
        else:
            print(f"direccion agregada: {direccion}")
            break
    #la cantidad total de dispensadores debe ser mayor a 0
    while True:
        six_l=int(input("Ingrese cantidad de Dispensadores de 6 lts. :"))
        if six_l<0:
            print("error ingrese numero valido")
        else:
            while True:
                ten_l=int(input("Ingrese cantidad de Dispensadores de 10 lts. : "))
                if  ten_l<0:
                    print("error ingrese numero valido")
                else:
                    while True:
                        veinte_l=int(input("Ingrese cantidad de Dispensadores de 20 lts. : "))
                        if veinte_l<0:
                            print("error ingrese numero valido")
                        else:
                            break
                    break
            pedido_total=six_l+ten_l+veinte_l
            if pedido_total<1:
                print("error,no puedes no pedir nada")
            else:
                print(f'''
pedido confimado:
              Disp.6lts:{six_l}
              Disp.10lts:{ten_l}
              Disp.20lts:{veinte_l}
''')
                break
    while True:
        paso=0
        sectores=int(input('''
seleccione sector:
                   1. Concepcion
                   2. Chiguayante
                   3. Talcahuano
                   4. Hualpen
                   5. San Pedro
'''))
        if sectores==1:
            sector="Concepcion"
            pass
        elif sectores==2:
            sector="Chiguayante"
            pass
        elif sectores==3:
            sector="Talcahuano"
            pass
        elif sectores==4:
            sector="Hualpen"
            pass
        elif sectores==5:
            sector="San Pedro"
            pass
        else:
            print("ingrese opcion valida")
        
        pedido={'id':id,
                'cliente':cliente,
                'direccion':direccion,
                'sector':sector,
                'six_l':six_l,
                'ten_l':ten_l,
                'veinte_l':veinte_l
        }
        pedidos.append(pedido)
        print(pedidos)
        #pedido=[{id},{cliente},{direccion},{sector},{six_l},{ten_l},{veinte_l}]
def listar_pedido():
    print("no listo")
def imprimir_hojaruta():
    print("no listo")
def busca_id():
    print("no listo")
while True:
    menu=int(input('''
    \t----CleanWasser---
    \tIngrese su seleccion:
    1. Registrar pedido
    2. Listar todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
        :'''))
    if menu ==1:
        registrar_pedido()
    elif menu ==2:
        print("Listar pedidos")
        pass
    elif menu ==3:
        print("Imprimir hoja de ruta")
        pass
    elif menu ==4:
        print("Buscar un pedido por ID")
        pass
    else:
        print("Finalizado ■-■")    
        import sys
        sys.exit()