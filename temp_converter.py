###some useful fxns
class TemperatureConverter:
    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def to_celsius(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        else:
            return self.temperature

    def to_fahrenheit(self):
        if self.unit == 'C':
            return(self.temperature * 9/5) + 32
        else:
            return self.temperature

    def convert(self, to_unit):
        if to_unit == 'C':
            return self.to_celsius()
        elif to_unit == 'F':
            return self.to_fahrenheit()
        else:
            return "Invalid unit"


### call function
t = TemperatureConverter(100, 'F')
print(t.to_celsius())
print(t.to_fahrenheit())
print(t.convert('C'))
