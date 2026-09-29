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

Cada push a `main` ejecuta GitHub Actions: instala dependencias, verifica la sintaxis del código y corre las pruebas con pytest. El workflow está en `.github/workflows/ci.yml`.

Si alguna prueba falla, el workflow se marca en rojo y bloquea la integración del cambio.
