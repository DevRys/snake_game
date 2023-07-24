import pygame
import random

ancho_pantalla = 640
alto_pantalla = 480

color_fondo = (0,0,0)
color_serpiente = (0,250,0)
color_comida = (255,0,0)

tamano_celda = 20

pygame.init()

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Snake Game")

reloj = pygame.time.Clock()

def juego():
  
  x = ancho_pantalla // 2
  y = alto_pantalla // 2
  
  velocidad_x = 0
  velocidad_y = 0
  
  serpiente = [(x, y)]
  
  comida_x = round(random.randint(0, ancho_pantalla - tamano_celda) 
                   / tamano_celda) * tamano_celda
  comida_y = round(random.randint(0, alto_pantalla - tamano_celda) 
                   / tamano_celda) * tamano_celda
  
  puntuacion = 0
  
  fin_juego = False
  
  while not fin_juego:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        fin_juego = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and velocidad_y != tamano_celda:
          velocidad_x = 0
          velocidad_y = -tamano_celda
        elif event.key == pygame.K_DOWN and velocidad_y != -tamano_celda:
          velocidad_x = 0 
          velocidad_y = tamano_celda
        elif event.key == pygame.K_LEFT and velocidad_x != tamano_celda:
          velocidad_x = -tamano_celda
          velocidad_y = 0
        elif event.key == pygame.K_RIGHT and velocidad_x != -tamano_celda:
          velocidad_x = tamano_celda
          velocidad_y = 0
    
    x += velocidad_x   
    y += velocidad_y   
    
    if x >= ancho_pantalla or x < 0 or y >= alto_pantalla or y < 0:
      fin_juego = True
      
    if (x, y) in serpiente[1:]:
      fin_juego = True
      
    serpiente.insert(0, (x, y))
    
    if x == comida_x and y == comida_y:
      puntuacion += 1
      comida_x = round(random.randint(0, ancho_pantalla - tamano_celda) 
                       / tamano_celda) * tamano_celda
      comida_y = round(random.randint(0, alto_pantalla - tamano_celda) 
                       / tamano_celda) * tamano_celda
    else: 
      serpiente.pop()
      
    pantalla.fill(color_fondo)
    for segmento in serpiente:
      pygame.draw.rect(pantalla, color_serpiente, (
        segmento[0], segmento[1], tamano_celda, tamano_celda
      ))
    pygame.draw.rect(pantalla, color_comida, (
        comida_x, comida_y, tamano_celda, tamano_celda
    ))
    
    pygame.display.flip()
    
    reloj.tick(10)
  
  print(f"Fin del juego, puntuacion: {puntuacion}")
  
  pygame.quit()
  
juego()

    