import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tareas import agregar_tarea, completar_tarea, listar_tareas


def test_agregar_tarea():
	tareas = []

	resultado = agregar_tarea(tareas, "Estudiar Python")

	assert resultado is tareas
	assert tareas == [{"descripcion": "Estudiar Python", "completada": False}]


def test_listar_tareas():
	tareas = [
		{"descripcion": "Estudiar Python", "completada": False},
		{"descripcion": "Entregar práctica", "completada": True},
	]

	assert listar_tareas(tareas) == [
		"1. [PEND] Estudiar Python",
		"2. [OK] Entregar práctica",
	]


def test_completar_tarea():
	tareas = [{"descripcion": "Estudiar Python", "completada": False}]

	resultado = completar_tarea(tareas, 1)

	assert resultado is tareas
	assert tareas[0]["completada"] is True
