class Entity:
    """
    Objeto genérico pra representar o player, inimigos, itens etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Mover a entidade por uma quantidade x
        self.x += dx
        self.y += dy
