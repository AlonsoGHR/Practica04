def agregar_tarea(tareas, descripcion):
	tareas.append({"descripcion": descripcion, "completada": False})
	return tareas


def listar_tareas(tareas):
	resultado = []
	for i, t in enumerate(tareas, start=1):
		estado = "OK" if t["completada"] else "PEND"
		resultado.append(f"{i}. [{estado}] {t['descripcion']}")
	return resultado


def completar_tarea(tareas, indice):
	tareas[indice - 1]["completada"] = True
	return tareas
