class Car:
    weight = 0

    def __init__(self):
        self.name = 'Car Mai'

    def __repr__(self):
        return f"{self.name}"

    def __call__(self, *args, **kwargs):
        return "This is from call"

    @classmethod
    def update_wight_value(cls, value):
        cls.weight = value

    @staticmethod
    def signal():
        return 'smth'

    @property
    def my_power(self):
        return self.power

    @my_power.setter
    def my_power(self, value):
        self.power = value

    @my_power.deleter
    def my_power(self):
        del self.power

