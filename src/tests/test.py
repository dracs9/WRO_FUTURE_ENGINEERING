from src.correction import cos_rule, calculate_correction
from umath import pi



def test_cos_rule():
    # print(cos_rule(3, 4, pi/2) - 5)
    assert abs(cos_rule(3, 4, pi/2) - 5) < 0.00001
    print("cos_rule pass")

test_cos_rule()