from pybricks.ev3devices import GyroSensor
# try:
    # from umath import sqrt, sin, cos, pi, asin
# except ImportError:
    # from math import sqrt, sin, cos, pi, asin

from umath import sqrt, sin, cos, pi, asin

class CorrectedGyro(GyroSensor):

    def __init__(self, port, correction=0):
        super().__init__(port)
        self.correction = 0

    def angle(self):
        return (super().angle() + self.correction)
    
    def angle_raw(self):
        return (super().angle())

def cos_rule(a, b, angle):
    return sqrt(a * a + b * b - (2 * a * b * cos(angle)))

def calculate_correction(a, l, d1, d2): #TODO: simplify and make it explanatory
    r = l / a

    # This is for odometry, it finds error vector
    # from current pos to target.
    # 
    # ls = r * sqrt(2 * (1 - cos(a)))
    # x = sqrt(ls*ls + l*l - (2 * l * ls * cos(a)))
    # b = (pi - a) / 2
    # ax = 1.5 * pi - asin((ls * sin(b)) / x)
    # pos -= vec(x * cos(ax), x * sin(ax))

    sd2 = d2 + r
    sd1 = d1 + r
    sd = cos_rule(sd1, sd2, a)
    correction_angle = asin((sd1 * sin(a)) / sd)
    return correction_angle