from random import randint

class Die():
    """代表骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回骰子面的随机数"""
        return randint(1,self.num_sides)

    