# main.py - Punto de entrada de la aplicación
from tareas import agregar_tarea, completar_tarea, listar_tareas


def main():
    print("=========================================")
    print("   SISTEMA DE GESTIÓN DE TAREAS (v1.0)   ")
    print("=========================================\n")

    # 1. Agregar tareas de prueba
    print("1. Agregando tareas iniciales...")
    agregar_tarea("Configurar repositorio en Git")
    agregar_tarea("Subir código inicial a GitHub")
    agregar_tarea("Documentar el archivo README.md")

    # 2. Listar las tareas actuales
    print("\n2. Estado inicial de las tareas:")
    listar_tareas()

    # 3. Marcar una tarea como completada
    print("3. Completando la primera tarea...")
    completar_tarea(1)

    # 4. Mostrar el estado actualizado
    print("\n4. Estado actualizado de las tareas:")
    listar_tareas()


if __name__ == "__main__":
    main()