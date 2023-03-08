###slearn about python class
class TemperatureConverter:
    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def to_celsius(self):
        '''this methods converts the temperature from Farenheit to Celius.
        If the temperature is in Celius it returns the Celcius temp
         '''
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        else:
            return self.temperature

    def to_fahrenheit(self):
        '''This method converts the temperature from Celcius to Farenheit
        If the temp is already in F it returns the F temp itself'''
        if self.unit == 'C':
            return(self.temperature * 9/5) + 32
        else:
            return self.temperature

    def convert(self, to_unit):
        '''This method takes an argument "to_unit", which can be either C or F
        and converts the temperature to that unit'''
        if to_unit == 'C':
            return self.to_celsius()
        elif to_unit == 'F':
            return self.to_fahrenheit()
        else:
            return "Invalid unit"


### call function
#i) create an instance "t" and the class in the instance take two arguments 
# - temperature and unit
t = TemperatureConverter(100, 'F')
print(t.to_celsius())
print(t.to_fahrenheit())
print(t.convert('C'))


t1 = TemperatureConverter(45, 'F')
print(f"the output is: {t1.convert('C')}")