from tareas import agregar_tarea, completar_tarea, listar_tareas


def main():
	tareas = []

	while True:
		print("\n1) Agregar tarea")
		print("2) Listar tareas")
		print("3) Completar tarea")
		print("4) Salir")
		opcion = input("Selecciona una opción: ").strip()

		if opcion == "1":
			descripcion = input("Descripción de la tarea: ").strip()
			agregar_tarea(tareas, descripcion)
			print("Tarea agregada.")
		elif opcion == "2":
			resultado = listar_tareas(tareas)
			if resultado:
				for tarea in resultado:
					print(tarea)
			else:
				print("No hay tareas.")
		elif opcion == "3":
			if not tareas:
				print("No hay tareas para completar.")
				continue

			try:
				indice = int(input("Número de tarea a completar: ").strip())
				completar_tarea(tareas, indice)
				print("Tarea completada.")
			except (ValueError, IndexError):
				print("Índice de tarea no válido.")
		elif opcion == "4":
			print("Hasta luego.")
			break
		else:
			print("Opción no válida.")


if __name__ == "__main__":
	main()
