from re import A, I


class Celular():
    def __init__(self, camara, marca, color):
        self.camara = camara
        self.marca = marca
        self.color = color
    def __str__(self):
        cel = "Camara de: {} - Marca: {} - Color: {}"
        return cel.format(self.camara, self.marca, self.color)

i = Celular("50 megapixeles", "Samsung s22", "Negro")
print(i)


class Animales():
    def __init__(self, animal, tamaño, velocidad):
        self.animal = animal
        self.tamaño = tamaño
        self.velocidad = velocidad
    def __str__(self):
        a = "El: {} Tiene un tamaño aproximado de: {} y su velocidad alcanza entre: {}"
        return a.format(self.animal, self.tamaño, self.velocidad)

animales1 = Animales("Guepardo", "1,1 - 1,5 m", "80 - 130 km/h")  
print(animales1)

