class Fruit:
    flavour = "sweet"

    def __init__(self, flavour, shelf_life, texture):
        self.flavour = flavour
        self.shelf_life = shelf_life
        self.texture = texture
    def taste_flavour(self):
        return f"Does orange juice contain {self.flavour} flavour?"
        