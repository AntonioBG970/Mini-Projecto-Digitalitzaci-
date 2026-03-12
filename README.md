Descripción
El proyecto está organizado siguiendo la estructura estándar de Django:

gestio/ → configuración del proyecto
core/ → aplicación principal donde se encuentran los modelos y la lógica
db.sqlite3 → base de datos
manage.py → script para ejecutar comandos del proyecto

Requisitos
Python 3
pip
Git (opcional, para clonar el repositorio)

Para comprobar que tienes instalado Python y pip puedes comprobarlo en la Terminal con:
python --version
pip --version

Pasos para su instalación
1. Clonar repositorio
git clone https://github.com/AntonioBG970/Mini-Projecto-Digitalitzaci-.git

2. Entrar en la carpeta del proyecto
cd Mini-Projecto-Digitalitzaci-

Ahora dentro de la carpeta haremos lo siguiente.
crear un entorno virtual:
python -m venv venv

Acto seguido, activarlo:
Windows → venv\Scripts\activate
Mac/Linux → source venv/bin/activate

Instalar sus dependencias:
pip install -r requirements.txt

Sus dependencias principales son:
- Django
- asgiref
- sqlparse
- tzdata

Ahora para ejecutar la migración para preparar la base de datos haces:
python manage.py migrate

Después iniciamos el servidor. Para ello ponemos:
python manage.py runserver

Por último, para acceder a la aplicación ves al navegador y escribes:
http://127.0.0.1:8000
