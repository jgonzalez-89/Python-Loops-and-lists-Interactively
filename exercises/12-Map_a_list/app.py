Celsius_values = [-2,34,56,-10]

def fahrenheit_values(x):
    value = (x * 1.8) + 32
    return value
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
