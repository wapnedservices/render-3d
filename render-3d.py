import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# definir los vertices y las caras limiteofes
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)

colores = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
)

# definir una textura basuca
def cargar_textura():
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    imagen = pygame.image.load('textura.jpg')  # Cambia la ruta de la textura
    imagen = pygame.transform.flip(imagen, False, True)
    imagen_data = pygame.image.tostring(imagen, 'RGB', True)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imagen.get_width(), imagen.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, imagen_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    return texture

# iniciar OpenGL
def iniciar_opengl():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glLight(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
    glLight(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))

# dibujar el cubo con texturas y iluminacion
def dibujar_cubo():
    for i, surface in enumerate(surfaces):
        x = surface[0]
        for vertex in surface[1:]:
            glColor3fv(colores[i])
            glTexCoord2f(0.0, 0.0)
            glVertex3fv(vertices[vertex])
            glTexCoord2f(1.0, 0.0)
            glVertex3fv(vertices[vertex])
            glTexCoord2f(1.0, 1.0)
            glVertex3fv(vertices[vertex])
            glTexCoord2f(0.0, 1.0)
            glVertex3fv(vertices[vertex])

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(vertices[vertex])
    glEnd()

# Función para el bucle
def bucle_principal():
    textura = cargar_textura()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    iniciar_opengl()
    bucle_principal()
