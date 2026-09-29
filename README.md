# Gestor de Tareas - Práctica 04

Aplicación de consola para agregar, listar y completar tareas.

## Estructura

```text
Practica04/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_tareas.py
├── .gitignore
├── main.py
├── pytest.ini
├── README.md
├── requirements.txt
└── tareas.py
```

## Uso

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Inicia el gestor:

```bash
python main.py
```

Ejecuta las pruebas:

```bash
pytest -v
```

## Integración Continua

El workflow de GitHub Actions se ejecuta en cada `push` a `main` y en cada
`pull_request`. Prepara Python 3.12, instala las dependencias, verifica la
sintaxis y ejecuta las pruebas.
