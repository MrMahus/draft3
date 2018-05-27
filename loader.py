import pygame
import os


class Loader:

    def __init__(self):

        self.tile_collection = {

            0       :   None,    # Tile Transparent
            1       :   None,    # Tile Grass
            2       :   None,    # Tile 2
            3       :   None,    # Tile 3
            4       :   None,    # Tile 4
            5       :   None,    # Tile 5
            6       :   None,    # Tile 6
            7       :   None,    # Tile 7
            8       :   None,    # Tile 8

        }

        self.world_maps = {}    # { "map_0_0.txt" : (surface, (x , y )) , ... }

        self.tile_width = 32
        self.tile_height = 32
        self.tile_rows = 20 - 1
        self.tile_cols = 20 - 1

        self.loadTilesFiles()
        self.loadMapsInMemory()


    def loadTilesFiles(self):

        for id in self.tile_collection:

            if os.path.exists("res/tiles/tile_" + str(id) + ".png") == True:

                self.tile_collection[id] =\
                    pygame.image.load("res/tiles/tile_" + str(id) + ".png").convert_alpha()

            else:
                self.tile_collection[id] = None


    def loadMapFile(self, _map_file):

        if os.path.exists("res/maps/"+str(_map_file)):

            file_map = open("res/maps/"+_map_file, "r")
            buffer = []

            for lines in file_map:
                buffer.append(lines.rstrip('\n'))

            file_map.close()

            current_layer = 1
            layer_1 = ''
            layer_2 = ''
            layer_3 = ''

            for element in buffer:

                if element == 'first_layer,':
                    current_layer = 1

                if element == 'second_layer,':
                    current_layer = 2

                if element == 'third_layer,':
                    current_layer = 3

                if current_layer == 1 and element != 'first_layer,':
                    layer_1 += element

                if current_layer == 2 and element != 'second_layer,':
                    layer_2 += element

                if current_layer == 3 and element != 'third_layer,':
                    layer_3 += element

            layer_1 = layer_1.replace(',', "")
            layer_1 = list(layer_1)

            layer_2 = layer_2.replace(',', "")
            layer_2 = list(layer_2)

            layer_3 = layer_3.replace(',', "")
            layer_3 = list(layer_3)

            map_infos = (layer_1, layer_2, layer_3)

            return map_infos

        else:
            # print("map file "+str(_map_index)+ " could not be read")
            return None


    def drawTileMap(self, _map_layers, _surface):

        if _map_layers != None:

            for layer in _map_layers:

                tile_xPos =  0
                tile_yPos =  0

                for cell in layer:
                    _surface.blit(self.tile_collection[int(cell)], (tile_xPos,tile_yPos))
                    if tile_xPos < self.tile_width*self.tile_cols:
                        tile_xPos += 32
                    else:
                        tile_xPos = 0
                        tile_yPos += 32


            return _surface



    def loadMapsInMemory(self):

        for map_file in os.listdir("res/maps"):
            if map_file.endswith(".txt"):

                layers_collection = self.loadMapFile(str(map_file))
                surface = pygame.Surface((640,640))
                surface = self.drawTileMap(layers_collection, surface)

                x = None
                y = None
                file_name = map_file

                file_name = file_name.replace(".txt","")
                file_name = file_name.replace("map_","")
                file_name = file_name.replace("_","")


                if len(file_name) == 2:
                    x = int(file_name[0])
                    y = int(file_name[1])
                elif len(file_name) == 4:
                    x = int(str(file_name[0]) + str(file_name[1]))
                    y = int(str(file_name[2]) + str(file_name[3]))

                elif len(file_name) == 3:
                    if file_name[0] == '-':
                        x = int(str(file_name[0]) + str(file_name[1]))
                        y = int(file_name[2])

                    elif file_name[1] == '-':
                        x = int(file_name[0])
                        y = int(str(file_name[1]) + str(file_name[2]))

                pos = (x,y)

                self.world_maps[pos] = surface

