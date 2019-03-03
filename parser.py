from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as f:
        for line in f:
            line = line.strip('\n')
            print(line)
            if(line == "line"):
                params = f.next()
                params = params.strip('\n')
                params = params.split(" ")
                add_edge(points, int(params[0]), int(params[1]), int(params[2]), int(params[3]), int(params[4]), int(params[5]))
            elif(line == "ident"):
                ident(transform)
            elif(line == "scale"):
                params = f.next()
                params = params.strip('\n')
                params = params.split(" ")
                scaler = make_scale(int(params[0]), int(params[1]), int(params[2]))
                matrix_mult(scaler, transform)
            elif(line == "move"):
                params = f.next()
                params = params.strip('\n')
                params = params.split(" ")
                transformer = make_translate(int(params[0]), int(params[1]), int(params[2]))
                matrix_mult(transformer, transform)
            elif(line == "rotate"):
                params = f.next()
                params = params.strip('\n')
                params = params.split(" ")
                if(params[0] == "z"):
                    print("rotating by z " + params[1])
                    rotater = make_rotZ(int(params[1]))
                    print_matrix(rotater)
                elif(params[0] == "y"):
                    print("rotating by y " + params[1])

                    rotater = make_rotY(int(params[1]))
                    print_matrix(rotater)
                elif(params[0] == "x"):
                    print("rotating by x " + params[1])
                    rotater = make_rotX(int(params[1]))
                    print_matrix(rotater)
                matrix_mult(rotater, transform)
            elif(line == "apply"):
                matrix_mult(transform, points)
            elif(line == "display"):
                clear_screen(screen)
                print_matrix(points)
                draw_lines(points, screen, color)
                display(screen)
            elif(line == "save"):
                clear_screen(screen)
                draw_lines(points, screen, color)
                params = f.next()
                params = params.strip('\n')
                display(screen)
                print(params[0])
                save_extension(screen, params)
            else:
                print ("params")

