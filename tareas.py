# tareas.py - Módulo para la gestión de tareas

# Lista global para guardar las tareas
lista_tareas = []


def agregar_tarea(descripcion):
    """Añade una nueva tarea a la lista."""
    tarea = {"id": len(lista_tareas) + 1, "descripcion": descripcion, "completada": False}
    lista_tareas.append(tarea)
    print(f"✅ Tarea agregada con éxito: '{descripcion}'")


def listar_tareas():
    """Muestra todas las tareas registradas."""
    if not lista_tareas:
        print("📂 No hay tareas registradas actualmente.")
        return

    print("\n--- LISTA DE TAREAS ---")
    for tarea in lista_tareas:
        estado = "✔ Completada" if tarea["completada"] else "❌ Pendiente"
        print(f"[{tarea['id']}] {tarea['descripcion']} - {estado}")
    print("------------------------\n")


def completar_tarea(id_tarea):
    """Marca una tarea como completada según su ID."""
    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            print(f"🎉 Tarea '{tarea['descripcion']}' marcada como completada.")
            return
    print(f"⚠️ No se encontró ninguna tarea con el ID: {id_tarea}")