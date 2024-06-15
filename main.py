from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from rocket import rocket, stars  
from utils import stroke_output  

# Global variables for animation and initial values
x = 0.0
x1 = 0.0
y1 = 0.1
z1 = 0.0
a1 = 0
y2 = 0
z2 = 0

def draw_scene(ang):
    global x, x1, y1, z1, a1, y2, z2

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -13.0)

    glPushMatrix()
    if ang <= 2:
        glRotatef(ang * 30, 1, 0, 0)
        glTranslatef(0, -2 + ang, 0)
    else:
        glRotatef(60, 1, 0, 0)
        glTranslatef(0, 0, 0)
    glScalef(0.5, 0.5, 0.5)
    rocket(x, x1, y1, z1, a1, y2, z2) 
    glPopMatrix()
    #earth
    glPushMatrix()
    glColor3f(0.3059, 0.5412, 0.6745)
    if x >= 6.5:
        glTranslatef(0, -18, -95)
        glRotatef(10 * x, 0, 1, 0)
    else:
        glTranslatef(0, -10 - x, -10 - 15 * x)
    glutSolidSphere(10, 100, 100)  
    glPopMatrix()

    # Draw stars
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(0, -ang, 0)
    stars()  
    glPopMatrix()

    glFlush()
    glutSwapBuffers()


def update_scene():
    global x, x1, y1, z1, a1, y2, z2

    x += 0.01
    if x >= 3:
        x1 += 0.1
        y1 += 0.1
        z1 += 0.01
        a1 += 3
    if x > 5:
        y2 -= 0.1
    if x > 5.5:
        z2 += 0.1

    draw_scene(x)


def init():
    glClearColor(0.0, 0.0, 0.0, 0)
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, 640 / 480, 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearDepth(2.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -13.0)
    stroke_output(-2.0, 1.7, "Click y/Y to launch the rocket")
    mat_ambient = [0.0, 1.0, 2.0, 1.0]
    mat_diffuse = [0.0, 1.5, 0.5, 1.0]
    mat_specular = [5.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    light_intensity = [1.7, 1.7, 1.7, 1.0]
    light_position = [0.0, 5.0, 0.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_intensity)

    glEnable(GL_COLOR_MATERIAL)
    glFlush()
    glutSwapBuffers()

def menu(id):
    if id == 2:
        glutIdleFunc(update_scene)
    elif id == 5:
        sys.exit(0)
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()

def keyboard(key, x, y):
    if key == b'y' or key == b'Y':
        glutIdleFunc(update_scene)
    elif key == b'n' or key == b'N':
        sys.exit(0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"rocket")
    glutDisplayFunc(display)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glutKeyboardFunc(keyboard)
    glutCreateMenu(menu)
    glutAddMenuEntry("Launch 'y'", 1)
    glutAddMenuEntry("Quit 'n'", 5)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    init()
    glutMainLoop()
    

if __name__ == "__main__":
    main()