Para lograr correr esta aplicación deberán tener instalado Python 3, algunas bibliotecas y creado el entorno virtual:

== bibliotecas necesarias ==

* numpy
* pygame
* virtualenv

Las mismas pueden ser instaladas utilizando el sistema de instalación de paquetes de Python: PIP


Instalar PIP en Linux (Debian, ubuntu, Mint y derivados):
========================================================

sudo apt install python3-pip

python3.8 -m pip install --upgrade pip


Instalar Virtualenv o actualizarlo:
==================================

pip3 install virtualenv
pip3 install --upgrade virtualenv

Crear el Virtual Env:
=====================
python3 -m venv .

Instalar bibliotecas:
=====================

pip3 install pygame
pip3 install numpy


Solucion de problemas 
=====================

En linux puede que les tire un error por no encontrar el comando "python", ya que lo llama "python3".

solucion 1: crear un enlace simpolico

	sudo ln -s /usr/bin/python3 /usr/bin/python

solucion 2: 

	anteponer el comando al archivo: python3 start.py

solucion 3:

	editar el header del archivo start.py para que tome el comando python3