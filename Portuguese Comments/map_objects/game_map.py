from random import randint
from map_objects.rectangle import Rect
from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # largura e altura (width and height) aleatórios
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # posição aleatória sem sair do mapa
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            # A class Rect ajuda muito com retângulos. Duh.
            new_room = Rect(x, y, w, h)

            # Dá uma olhada nas outras salas e vê se interseccionam com a atual
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                    # Se não intersecciona, é válido.
                    # Criar a sala:
                self.create_room(new_room)
                    # Pega as coordenadas centrais da sala. útil pra depois
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                        # Primeira sala, onde o player começa.
                        player.x = new_x
                        player.y = new_y
                else:
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                        # Todas salas depois da primeira conectarão-se por túneis.
                        # Coordenadas centrais:

                        # Gera um número entre 0 e 1:
                    if randint(0, 1) == 1:
                        # Primeiro movimento horizontal, daí vertical
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)       
                    else:
                        # Primeiro movimento vertical, daí horizontal
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                        
                #Bota a sala nova numa lista.
            rooms.append(new_room)
            num_rooms += 1
                        
    def create_room(self, room):
        # passe pelas tiles do retângulo
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
