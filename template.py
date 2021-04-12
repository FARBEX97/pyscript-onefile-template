# ESPECIFICACIONES
# Saluda y despide al usuario a través de la consola.
# Requiere pasar un objeto string como argumento.
# Devuelve la variable "nombre".

# TODO's:
# - Añadir una función que imprima en pantalla la siguiente pregunta: "¿Cuál es tu color favorito?"

# DEPENDENCIAS
import dependencia    # pip install dependencia

# CONFIGURACIÓN
TU_NOMBRE = 'Rey Arturo'

# FUNCIÓN PRINCIPAL
def main(nombre):
    saludar(nombre)
    despedir(nombre)
    return nombre

# IMPLEMENTACIÓN
def saludar(nombre):
    """Descripción de la función"""
    print('Hola, ' + nombre + '.')

def despedir(nombre):
    """Descripción de la función"""
    print('Adiós, ' + nombre + '.')

if __name__ == "__main__":
    nombre = TU_NOMBRE
    main(nombre)
