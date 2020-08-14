class Tile:
#"""
#Tile: quadrado no mapa. Pode ou não bloquear seu movimento (parede, poço de lava), e pode ou não bloquear visão.
#"""
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        
        # Por padrão, se uma tile tá bloqueado por algo (parede, por exemplo), também bloqueia sua visão.
        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight
    