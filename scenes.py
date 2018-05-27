
class Map:

    def __init__(self, _display_settings):

        self.map_size = _display_settings






    def draw(self, _loader, _display, _player_pos):



        x_world = int(-_player_pos[0] / 320)
        y_world = int(-_player_pos[1] / 320)

        current_map_pos = (x_world, y_world)
        north_map = (current_map_pos[0], current_map_pos[1]-1)
        west_map = (current_map_pos[0]-1, current_map_pos[1])
        east = (current_map_pos[0]+1, current_map_pos[1]-1)
        south = (current_map_pos[0], current_map_pos[1]+1)


        if current_map_pos in _loader.world_maps:
            _display.blit(_loader.world_maps[current_map_pos], (_player_pos[0],_player_pos[1]))







        '''if north_map in _loader.world_maps:
            _display.blit(_loader.world_maps[north_map], (_player_pos[0],_player_pos[1] - 640))
        if west_map in _loader.world_maps:
            _display.blit(_loader.world_maps[west_map], (_player_pos[0]-640,_player_pos[1]))
        if east in _loader.world_maps:
            _display.blit(_loader.world_maps[east], (_player_pos[0]+640,_player_pos[1]))
        if south in _loader.world_maps:
            _display.blit(_loader.world_maps[south], (_player_pos[0],_player_pos[1]+640))'''




