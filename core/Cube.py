import math

class Cube:
    def __init__(self, pos=[0,0,0], scale=[1,1,1]):
        self.position = pos
        self.scale = scale
        #self.RotationMatrix3d = self.Find3dRotationMatrix()
        self.rotation = [0,0,0]
        self.rotatedPoints = [[self.position[0], self.position[1], self.position[2]],                               #1
                  [self.position[0]+self.scale[0], self.position[1], self.position[2]],                             #2
                  [self.position[0]+self.scale[0], self.position[1]+self.scale[1], self.position[2]],               #3
                  [self.position[0], self.position[1]+self.scale[1], self.position[2]],                             #4
                  [self.position[0], self.position[1]+self.scale[1], self.position[2]+self.scale[2]],               #5
                  [self.position[0]+self.scale[0], self.position[1]+self.scale[1], self.position[2]+self.scale[2]], #6
                  [self.position[0]+self.scale[0], self.position[1], self.position[2]+self.scale[2]],               #7
                  [self.position[0], self.position[1], self.position[2]+self.scale[2]]]                             #8
        
        
        self.points = [[self.position[0], self.position[1], self.position[2]],                                      #1
                  [self.position[0]+self.scale[0], self.position[1], self.position[2]],                             #2
                  [self.position[0]+self.scale[0], self.position[1]+self.scale[1], self.position[2]],               #3
                  [self.position[0], self.position[1]+self.scale[1], self.position[2]],                             #4
                  [self.position[0], self.position[1]+self.scale[1], self.position[2]+self.scale[2]],               #5
                  [self.position[0]+self.scale[0], self.position[1]+self.scale[1], self.position[2]+self.scale[2]], #6
                  [self.position[0]+self.scale[0], self.position[1], self.position[2]+self.scale[2]],               #7
                  [self.position[0], self.position[1], self.position[2]+self.scale[2]]]                             #8
        
        
        self.faces = [
            [self.points[0], self.points[1], self.points[2], self.points[3]],          #1
            [self.points[1], self.points[6], self.points[5], self.points[2]],          #2
            [self.points[4], self.points[5], self.points[6], self.points[7]],          #3
            [self.points[3], self.points[4], self.points[7], self.points[0]],          #4
            [self.points[0], self.points[1], self.points[6], self.points[7]],          #5
            [self.points[3], self.points[2], self.points[5], self.points[4]],          #6
        ]
        
        self.centreFaces = [
            [self.points[0][0]+self.scale[0]/2, self.points[0][1]+self.scale[1]/2, self.points[0][2]],          #1
            [self.points[1][0], self.points[1][1]+self.scale[1]/2, self.points[1][2]+self.scale[2]/2],          #2
            [self.points[6][0]-self.scale[0]/2, self.points[6][1]+self.scale[1]/2, self.points[6][2]],          #3
            [self.points[7][0], self.points[7][1]+self.scale[1]/2, self.points[7][2]-self.scale[2]/2],          #4
            [self.points[0][0]+self.scale[0]/2, self.points[0][1], self.points[0][2]+self.scale[2]/2],          #5
            [self.points[3][0]+self.scale[0]/2, self.points[3][1], self.points[3][2]+self.scale[2]/2],          #6
        ]
        
        
        
        self.rotatedFaces = [
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[2], self.rotatedPoints[3]],          #1
            [self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[5], self.rotatedPoints[2]],          #2
            [self.rotatedPoints[4], self.rotatedPoints[5], self.rotatedPoints[6], self.rotatedPoints[7]],          #3
            [self.rotatedPoints[3], self.rotatedPoints[4], self.rotatedPoints[7], self.rotatedPoints[0]],          #4
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[7]],          #5
            [self.rotatedPoints[3], self.rotatedPoints[2], self.rotatedPoints[5], self.rotatedPoints[4]],          #6
        ]
        
    
    def rotateSingleX(self, vector, theta, centre=[0,0]):
        point = vector
        math.radians(theta)
        for i in range(0, len(self.rotatedPoints)):
            x = vector[0]
            y = ((vector[1]-centre[0]) * math.cos(theta)) - ((vector[2]-centre[1]) * math.sin(theta))
            z = ((vector[1]-centre[0]) * math.sin(theta)) + ((vector[2]-centre[1]) * math.cos(theta))
            
        return [x, y, z]
    
    def rotateSingleY(self, vector, theta, centre=[0,0]):
        point = vector
        math.radians(theta)
        for i in range(0, len(self.rotatedPoints)):
            x = ((vector[0]-centre[0]) * math.cos(theta)) + ((vector[2]-centre[1]) * math.sin(theta))
            y = vector[1]
            z = ((vector[0]-centre[0]) * -math.sin(theta)) + ((vector[2]-centre[1]) * math.cos(theta))
            
        return [x, y, z]
    
    
    def project(self, screen, camera, face):      
        self.rotatedFaces = [
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[2], self.rotatedPoints[3]],          #1
            [self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[5], self.rotatedPoints[2]],          #2
            [self.rotatedPoints[4], self.rotatedPoints[5], self.rotatedPoints[6], self.rotatedPoints[7]],          #3
            [self.rotatedPoints[3], self.rotatedPoints[4], self.rotatedPoints[7], self.rotatedPoints[0]],          #4
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[7]],          #5
            [self.rotatedPoints[3], self.rotatedPoints[2], self.rotatedPoints[5], self.rotatedPoints[4]]           #6
        ]
        
        
        
        position2d = []
        for point in face:
            rotatedPoint = self.rotateAll(theta=[camera.rotation[0], camera.rotation[1], 0], centre=[camera.position], point=point)
            deltaX = rotatedPoint[0] - camera.position[0]
            deltaY = rotatedPoint[1] - camera.position[1]
            deltaZ = rotatedPoint[2] - camera.position[2]
            focalLength = screen.focalLength
            
            x = (focalLength * deltaX) // (deltaZ + focalLength)+screen.size[0]/2
            y = (focalLength * deltaY) // (deltaZ + focalLength)+screen.size[1]/2
            position2d.append([x, y])
        return position2d
    
    
    def projectsinglepoint(self, screen, camera, face):      
        self.rotatedFaces = [
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[2], self.rotatedPoints[3]],          #1
            [self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[5], self.rotatedPoints[2]],          #2
            [self.rotatedPoints[4], self.rotatedPoints[5], self.rotatedPoints[6], self.rotatedPoints[7]],          #3
            [self.rotatedPoints[3], self.rotatedPoints[4], self.rotatedPoints[7], self.rotatedPoints[0]],          #4
            [self.rotatedPoints[0], self.rotatedPoints[1], self.rotatedPoints[6], self.rotatedPoints[7]],          #5
            [self.rotatedPoints[3], self.rotatedPoints[2], self.rotatedPoints[5], self.rotatedPoints[4]]           #6
        ]
        
        
        
        position2d = []
        deltaX = face[0] - camera.position[0]
        deltaY = face[1] - camera.position[1]
        deltaZ = face[2] - camera.position[2]
        focalLength = screen.focalLength
            
        x = (focalLength * deltaX) // (deltaZ + focalLength)+screen.size[0]/2
        y = (focalLength * deltaY) // (deltaZ + focalLength)+screen.size[1]/2
        position2d = [x, y]
        return position2d
    

    def drawWire(self, screen, camera):
        draw = True
        for face in self.rotatedFaces:
            draw = True
            for point in face:
                if camera.position[2]-point[2] > 500:
                    draw = False
                    
            if draw == True:
                drawingpoints = self.project(screen, camera, face)
                screen.Canvas.create_polygon(drawingpoints, outline="cyan", width=1, fill="")
            
        for point in self.centreFaces:
            drawcentreface = self.projectsinglepoint(screen, camera, point)
            screen.Canvas.create_oval(drawcentreface[0]-1, drawcentreface[1]-1, drawcentreface[0]+1, drawcentreface[1]+1, fill="cyan")
        
                
            
    def rotateX(self, theta, centre=[0,0]):
        self.rotation[0] += theta
        math.radians(theta)
        for i in range(0, len(self.rotatedPoints)):
            x = self.rotatedPoints[i][0]
            y = ((self.rotatedPoints[i][1]-centre[0]) * math.cos(theta)) - ((self.rotatedPoints[i][2]-centre[1]) * math.sin(theta))
            z = ((self.rotatedPoints[i][1]-centre[0]) * math.sin(theta)) + ((self.rotatedPoints[i][2]-centre[1]) * math.cos(theta))
            self.rotatedPoints[i] = [x, y+centre[0], z+centre[1]]
        for i in range(0, len(self.centreFaces)):
            x=self.centreFaces[i][0]
            y=((self.centreFaces[i][1]-centre[0]) * math.cos(theta)) - ((self.centreFaces[i][2]-centre[1]) * math.sin(theta))
            z=((self.centreFaces[i][1]-centre[0]) * math.sin(theta)) + ((self.centreFaces[i][2]-centre[1]) * math.cos(theta))
            self.centreFaces[i] = [x,y+centre[0],z+centre[1]]
        
    def rotateY(self, theta, centre=[0,0]):
        self.rotation[1] += theta
        math.radians(theta)
        for i in range(0, len(self.rotatedPoints)):
            x = ((self.rotatedPoints[i][0]-centre[0]) * math.cos(theta)) + ((self.rotatedPoints[i][2]-centre[1]) * math.sin(theta))
            y = self.rotatedPoints[i][1]
            z = ((self.rotatedPoints[i][0]-centre[0]) * -math.sin(theta)) + ((self.rotatedPoints[i][2]-centre[1]) * math.cos(theta))
            self.rotatedPoints[i] = [x+centre[0], y, z+centre[1]]
        for i in range(0, len(self.centreFaces)):
            x = ((self.centreFaces[i][0]-centre[0]) * math.cos(theta)) + ((self.centreFaces[i][2]-centre[1]) * math.sin(theta))
            y = self.centreFaces[i][1]
            z = ((self.centreFaces[i][0]-centre[0]) * -math.sin(theta)) + ((self.centreFaces[i][2]-centre[1]) * math.cos(theta))
            self.centreFaces[i] = [x+centre[0], y, z+centre[1]]
            
    def rotateZ(self, theta, centre=[0,0]):
        self.rotation[2] += theta
        math.radians(theta)
        for i in range(0, len(self.rotatedPoints)):
            x = ((self.rotatedPoints[i][0]-centre[0]) * math.cos(theta)) - ((self.rotatedPoints[i][1]-centre[1]) * math.sin(theta))
            y = ((self.rotatedPoints[i][0]-centre[0]) * math.sin(theta)) + ((self.rotatedPoints[i][1]-centre[1]) * math.cos(theta))
            z = self.rotatedPoints[i][2]
            self.rotatedPoints[i] = [x+centre[0], y+centre[1], z]
        for i in range(0, len(self.centreFaces)):
            x = ((self.centreFaces[i][0]-centre[0]) * math.cos(theta)) - ((self.centreFaces[i][1]-centre[1]) * math.sin(theta))
            y = ((self.centreFaces[i][0]-centre[0]) * math.sin(theta)) + ((self.centreFaces[i][1]-centre[1]) * math.cos(theta))
            z = self.centreFaces[i][2]
            self.centreFaces[i] = [x+centre[0], y+centre[1], z]
    
    
    def rotateAll(self, theta=[0,0,0], centre=[0,0,0], point=[0,0,0]):
        for rotation in theta:
            rotation = math.radians(rotation)
        part1 = self.MatrixMultiplication3x3([[math.cos(theta[2]), -math.sin(theta[2]), 0],
                                      [math.sin(theta[2]), math.cos(theta[0]), 0],
                                      [0, 0, 1]],
                                     
                                     
                                     [[math.cos(theta[1]), 0, math.sin(theta[1])],
                                      [0, 1, 0],
                                      [-math.sin(theta[1]), 0, math.cos(theta[1])]])
        
        fullRotation = self.MatrixMultiplication3x3(part1, [[1, 0, 0],
                                                            [0, math.cos(theta[2]), -math.sin(theta[2])],
                                                            [0, math.sin(theta[2]), math.cos(theta[2])]])
        print(centre)
        x = fullRotation[0][0]*(point[0]-centre[0][0]) + fullRotation[0][1]*(point[1]-centre[0][1]) + fullRotation[0][2]*(point[2]-centre[0][2])
        y = fullRotation[1][0]*(point[0]-centre[0][0]) + fullRotation[1][1]*(point[1]-centre[0][1]) + fullRotation[1][2]*(point[2]-centre[0][2])
        z = fullRotation[2][0]*(point[0]-centre[0][0]) + fullRotation[2][1]*(point[1]-centre[0][1]) + fullRotation[2][2]*(point[2]-centre[0][2])
        returnPoint = [x+centre[0][0], y+centre[0][1], z+centre[0][2]]
        
        return returnPoint
        
    
    
    def MatrixMultiplication3x3(self, Matrix1, Matrix2):
        RM  = [[0,0,0], [0,0,0], [0,0,0]]

        matrix_length = len(Matrix1)
        for i in range(len(Matrix1)):
            for j in range(len(Matrix2[0])):
                for k in range(len(Matrix2)):
                    RM[i][j] += Matrix1[i][k] * Matrix2[k][j]
    
        return RM   
    
    
    def _3dpythag(self, a, b, c):
        return math.sqrt((a**2)+(b**2)+(c**2))