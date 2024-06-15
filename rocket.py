# rocket.py

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def rocket(x, x1, y1, z1, a1, y2, z2):
    # Main top cone
    glPushMatrix()
    if x >= 5.5:
        glTranslatef(z2, -z2, z2)
        glRotatef(a1, 0, 1, 1)
    glPushMatrix()
    glTranslatef(0, 2.5, 0)
    glColor3f(1, 0, 0)
    glScalef(2.2, 1.5, 2.2)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPopMatrix()

    # Satellite container
    glPushMatrix()
    if x >= 6.8:
        glTranslatef(2, 0, 0)
        glRotatef(x * 40, 0, 1, 0)
    # satellite()
    glPopMatrix()
    glPushMatrix()
    if x >= 5:
        glTranslatef(0, y2, y2)
        glRotatef(a1, 0, 1, 1)
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(0, 0.0, 0)
    glScalef(0.3, 4.3, 0.3)
    glRotatef(90, 1, 0, 0)
    glutSolidTorus(0.5, 1, 30, 30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, -2.2, 0)
    glColor3f(1, 0, 0)
    glScalef(3, 1.5, 3)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPopMatrix()

    # RightSide rocket
    glPushMatrix()
    glTranslatef(x1, -y1, z1)
    glRotatef(a1, 0, 1, 1)
    glPushMatrix()
    glTranslatef(0.7, 1, 0)
    glColor3f(1, 0, 0)
    glScalef(1.5, 1, 1.5)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.7, -0.2, 0)
    glColor3f(1, 1, 1)
    glScalef(0.2, 6.5, 0.2)
    glRotatef(90, 1, 0, 0)
    glutSolidTorus(0.2, 1, 30, 30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.7, -2.0, 0)
    glColor3f(1, 0, 0)
    glScalef(1.5, 1, 1.5)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPopMatrix()

    # LeftSide rocket
    glPushMatrix()
    glTranslatef(-x1, -y1, -z1)
    glRotatef(-a1, 0, 1, 1)
    glPushMatrix()
    glTranslatef(-0.7, 1, 0)
    glColor3f(1, 0, 0)
    glScalef(1.5, 1, 1.5)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-0.7, -0.2, 0)
    glColor3f(1, 1, 1)
    glScalef(0.2, 6.5, 0.2)
    glRotatef(90, 1, 0, 0)
    glutSolidTorus(0.2, 1, 30, 30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-0.7, -2.0, 0)
    glColor3f(1, 0, 0)
    glScalef(1.5, 1, 1.5)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(0.2, 1, 30, 30)
    glPopMatrix()
    glPopMatrix()

def stars():
    for s1 in range(50, 1000, 4):
        for s2 in range(-60, 60, 5):
            glPushMatrix()
            glBegin(GL_POINTS)
            glVertex3f(s2 / 10.0, s1 / 10.0, 0)
            glEnd()
            glPopMatrix()
    for s3 in range(52, 1000, 3):
        for s4 in range(-62, 60, 3):
            glPushMatrix()
            glBegin(GL_POINTS)
            glVertex3f(s4 / 10.0, s3 / 10.0, 0)
            glEnd()
            glPopMatrix()
