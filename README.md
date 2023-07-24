# Snake Game

Este es un sencillo juego de Snake creado utilizando la biblioteca Pygame en Python.

## Descripción

El juego consiste en controlar una serpiente que se mueve en una cuadrícula y debe comer alimentos (representados por celdas rojas) para crecer. La serpiente se mueve con las teclas de dirección (arriba, abajo, izquierda, derecha) y debe evitar chocar contra los bordes de la pantalla o contra sí misma. El objetivo es conseguir la mayor puntuación posible comiendo alimentos antes de que ocurra una colisión.

## Instrucciones

1. Instala la biblioteca Pygame si aún no la tienes instalada: `pip install pygame`
2. Ejecuta el script y el juego comenzará automáticamente.
3. Usa las teclas de dirección (arriba, abajo, izquierda, derecha) para mover la serpiente.
4. Trata de comer los alimentos (celdas rojas) para aumentar la puntuación.
5. El juego terminará cuando la serpiente choque con los bordes de la pantalla o consigo misma.
6. La puntuación se mostrará al final del juego.

## Generar ejecutable 
1. Instalar la biblioteca `pip install pyinstaller`
2. Ejecuta el siguiente comando `pyinstaller snake.py --onefile -w`
3. Se crearán dos carpetas "build" y "dist"
4. Dentro de dist estará tu archivo ejecutable

## Requisitos

- Python 3.x
- Pygame

## Licencia

[MIT License](https://opensource.org/licenses/MIT)
