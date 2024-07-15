from random import randint
from os import system
import csv
from statistics import geometric_mean

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez',
                'Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

base_datos = []

def asignar_sueldos():
    system('cls')
    for trabajador in trabajadores:
        datos = {'Nombre': trabajador,
                 'Sueldo': randint(300_000, 2_500_000)}
        base_datos.append(datos)
    input('Sueldos generados con éxito.\nPresione Enter para continuar...')

def clasificar_sueldos():
    system('cls')
    if base_datos:
        menor800 = []
        menor2_000_000 = []
        mayor2_000_000 = []

        for dato in base_datos:
            if dato['Sueldo'] < 800_000:
                menor800.append(dato)
            elif dato['Sueldo'] < 2_000_000:
                menor2_000_000.append(dato)
            else:
                mayor2_000_000.append(dato)

        print(f'\nSueldos menores a $800.000\nTOTAL: {len(menor800)}\n')
        if len(menor800) > 0:
            print(f'Nombre empleado\t\tSueldo')
        for dato in menor800:
            print(f'{dato['Nombre']}\t\t${dato['Sueldo']}')

        print(f'\nSueldos entre $800.000 y $2.000.000\nTOTAL: {len(menor2_000_000)}\n')
        if len(menor2_000_000) > 0:
            print(f'Nombre empleado\t\tSueldo')
        for dato in menor2_000_000:
            print(f'{dato['Nombre']}\t\t${dato['Sueldo']}')

        print(f'\nSueldos superiores a $2.000.000\nTOTAL: {len(mayor2_000_000)}\n')
        if len(mayor2_000_000) > 0:
            print(f'Nombre empleado\t\tSueldo')
        for dato in mayor2_000_000:
            print(f'{dato['Nombre']}\t\t${dato['Sueldo']}')
    else:
        print('No se han asignado sueldos a los trabajadores.')
    input('Presione Enter para continuar...')

def menu_estadisticas():
    system('cls')
    if base_datos:
        while True:
            try:
                print('[1] Sueldo más alto\n'
                    '[2] Sueldo más bajo\n'
                    '[3] Promedio de sueldos\n'
                    '[4] Media geométrica')
                op_menu = int(input(': '))
            except ValueError:
                print('Ingrese únicamente el dígito de la opción que desea.\n')
                continue
            if 1 <= op_menu <= 4:
                break
            else:
                print('La opción seleccionada no es válida.\n')
        ver_estadisticas(op_menu)
    else:
        print('No se han asignado sueldos a los trabajadores.')
        input('Presione Enter para continuar...')
def ver_estadisticas(opcion):
    system('cls')
    if opcion == 1:
        #Sueldo más alto
        sueldo_alto = base_datos[0]

        for i in range(len(base_datos)):
            if base_datos[i]['Sueldo'] > sueldo_alto['Sueldo']:
                sueldo_alto = base_datos[i]
        print('Sueldo más alto:\n'
            f'{sueldo_alto['Nombre']}\t${sueldo_alto['Sueldo']}')
    elif opcion == 2:    
        #Sueldo más bajo
        sueldo_bajo = base_datos[0]

        for i in range(len(base_datos)):
            if base_datos[i]['Sueldo'] < sueldo_bajo['Sueldo']:
                sueldo_bajo = base_datos[i]
        print('Sueldo más bajo:\n'
            f'{sueldo_bajo['Nombre']}\t${sueldo_bajo['Sueldo']}')
    elif opcion == 3:    
        #Promedio sueldos
        acumulador_sueldos = 0

        for dato in base_datos:
            acumulador_sueldos += dato['Sueldo']
        promedio_sueldos = round(acumulador_sueldos/len(base_datos))

        print(f'El promedio de los sueldos es:\n${promedio_sueldos}')
    elif opcion == 4:
        #Media geométrica
        lista_sueldos = []
        for dato in base_datos:
            lista_sueldos.append(dato['Sueldo'])

        media_geometrica = round(geometric_mean(lista_sueldos))

        print(f'Media geométrica:\n${media_geometrica}')

    input('Presione Enter para continuar...')
    
def reporte_sueldos():
    system('cls')
    if base_datos:
        print('Nombre empleado\t\tSueldo Base\tDescuento Salud\t\tDescuento AFP\t\tSueldo Líquido')

        #Lista para archivo CSV
        lista_datos = [['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Líquido']]

        for dato in base_datos:
            sueldo_base = dato['Sueldo']
            desc_salud = round(sueldo_base * 0.07) # 7% de descuento
            desc_afp = round(sueldo_base * 0.12) # 12% de descuento
            sueldo_liquido = sueldo_base - (desc_salud + desc_afp)

            print(f'{dato['Nombre']}\t\t${sueldo_base}\t\t${desc_salud}\t\t\t${desc_afp}\t\t\t${sueldo_liquido}')
            lista_datos.append([dato['Nombre'],f'${sueldo_base}',f'${desc_salud}',f'${desc_afp}',f'${sueldo_liquido}'])
        
        with open('Reporte_sueldos.csv','w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)

            escritor.writerows(lista_datos)
        print('\nSe han exportado los datos a Reporte_sueldos.csv para facilitar su lectura.')
    else:
        print('No se han asignado sueldos a los trabajadores.')
    input('Presione Enter para continuar...')

def salir_programa():
    system('cls')
    print('Finalizando programa...\n'
          'Desarrollado por Matías Arancibia\n'
          'RUT 21.339.610-2')

def menu():
    while True:
        system('cls')
        while True:
            try:
                print('[1] Asignar sueldos aleatorios\n'
                      '[2] Clasificar sueldos\n'
                      '[3] Ver estadísticas\n'
                      '[4] Reporte de sueldos\n'
                      '[5] Salir del programa')
                op_menu = int(input(': '))
            except ValueError:
                print('Ingrese únicamente el dígito de la opción que desee.\n')
                continue
            if 1 <= op_menu <= 5:
                break
            else:
                print('La opción seleccionada no es válida.\n')
        if op_menu == 1:
            asignar_sueldos()
        elif op_menu == 2:
            clasificar_sueldos()
        elif op_menu == 3:
            menu_estadisticas()
        elif op_menu == 4:
            reporte_sueldos()
        else:
            salir_programa()
            break

if __name__ == '__main__':
    menu()