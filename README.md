# Calculadora

Aplicación "mock" para asignación de CI/CD pipeline usango Github Actions

## Prerequisitos
1. Tener instalado python 3.7+ en su dispositivo

## Instalación
1. Descargar el repositorio 
2. En el repositorio, crear un ambiente virtual con el siguiente comando: `python -m .venv` (en su terminal puede ser `python` o `python3`, depende de su configuracion)
3. Inicializar el ambiente virtual con el siguiente comando: `source .venv/bin/activate`
4. Instalar dependencias en el ambiente virtual con el siguiente comando: `pip install -r requirements.txt`

## Uso
Una vez realizado los pasos de instalación y con el ambiente virtual activado en su terminal puede utilizar los siguiente comandos:
- `python Calculadora.py`: corre el programa en su terminal.
- `pytest -v`: corre las pruebas unitarias del programa y muestra un log de cada una de ellas


## Referencias
1. https://docs.python.org/3/library/venv.html
2. https://docs.pytest.org/en/7.4.x/getting-started.html
