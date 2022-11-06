import tkinter; import time; import keyboard

class Window(tkinter.Tk):
    def __init__(self, size=[480, 480], focalLength=1):
        super().__init__()
        self.Canvas = tkinter.Canvas(self, width=size[0], height=size[1], background="black")
        self.Canvas.pack()
        self.state("zoomed")
        self.resizable(False, False)
        self.focalLength = focalLength
        self.size = size
    
    def main(self, cube, camera):
        while True:
            
            if keyboard.is_pressed("w"):
                camera.position[2] += 50
            if keyboard.is_pressed("s"):
                camera.position[2] -= 50
            if keyboard.is_pressed("space"):
                camera.position[1] -= 50
            if keyboard.is_pressed("ctrl"):
                camera.position[1] += 50
            if keyboard.is_pressed("a"):
                camera.position[0] -= 50
            if keyboard.is_pressed("d"):
                camera.position[0] += 50
            self.Canvas.delete("all")
            
            
            if keyboard.is_pressed("i"):
                camera.rotation[1] += 0.1
            if keyboard.is_pressed("k"):
                camera.rotation[1] -= 0.1
            
            
            cube.rotateZ(0.01, [cube.position[0]+cube.scale[0]/2, cube.position[1]+cube.scale[1]/2])
            cube.rotateX(0.005, [cube.position[1]+cube.scale[1]/2, cube.position[2]+cube.scale[2]/2])
            cube.rotateY(0.025, [cube.position[0]+cube.scale[0]/2, cube.position[2]+cube.scale[2]/2])
            cube.drawWire(screen=self, camera=camera)
            self.update()
            
            time.sleep(0.01)