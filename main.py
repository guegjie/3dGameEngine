import core.Camera; import core.Cube; import core.Screen;

def __main__():
    cube = core.Cube.Cube(pos=[-63,-63,63], scale=[63*2, 63*2, 63*2])
    window = core.Screen.Window(focalLength=500, size=[1920,1080])
    camera = core.Camera.Camera(pos=[0,0,0])
    window.main(cube, camera)
    

__main__()