# Todo: Code is a bit unclear

def fahr_to_celsius(fahr):
    celcius = (fahr - 32) * (5 / 9)
    return celcius

def fahr_to_kelvin(fahr):
    celcius = fahr_to_celsius(fahr)
    kelvin = celcius + 273.15
    return kelvin

# print(fahrenheit_to_celcius(212))   # Expect 100.0
# print(fahrenheit_to_kelvin(32))     # Expect 273.15