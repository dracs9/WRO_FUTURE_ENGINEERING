from pybricks.ev3devices import GyroSensor

class CorrectedGyro(GyroSensor):

    def __init__(self, port, correction=0):
        super().__init__(port)
        self.correction = 0

    def angle(self):
        return (super().angle() + self.correction)
    
    def angle_raw(self):
        return (super().angle())