import pygame

class Player:

    def __init__(self):
        self.life_points = 10
        self.inventory = []

        self.player_position_x = 0
        self.player_position_y = 0
        self.velocity = 3

        self.player_width = 32
        self.play_height = 32
        self.playerSurface = pygame.Surface((self.player_width, self.play_height))
        self.playerSurface.fill((255,0,0))

        self.key_states = None

        self.direction = None




    def move_player(self):


        if self.key_states["up"] == True:
            self.player_position_y -= self.velocity
            self.direction = "north"

        if self.key_states["down"] == True:
            self.player_position_y += self.velocity
            self.direction = "south"

        if self.key_states["left"] == True:
            self.player_position_x -= self.velocity
            self.direction ="west"

        if self.key_states["right"] == True:
            self.player_position_x += self.velocity
            self.direction = "east"

        if self.key_states["up_left"] == True:
            self.player_position_x -= self.velocity / 2
            self.player_position_y -= self.velocity / 2

        if self.key_states["up_right"] == True:
            self.player_position_x += self.velocity / 2
            self.player_position_y -= self.velocity / 2

        if self.key_states["down_left"] == True:
            self.player_position_x -= self.velocity / 2
            self.player_position_y += self.velocity / 2

        if self.key_states["down_right"] == True:
            self.player_position_x += self.velocity / 2
            self.player_position_y += self.velocity / 2





    # Draw
    def drawPlayer(self,_game_display, _display_size):

         _game_display.blit(self.playerSurface, (_display_size[0]/2,_display_size[1]/2))



    # Update
    def updatePlayer(self, _key_states):
        self.setkeyStates(_key_states)
        self.move_player()


    # Setters

    def setkeyStates(self, _key_state):
        self.key_states = _key_state


    # Getters

    def getPlayerPos(self):
        return(-self.player_position_x,-self.player_position_y)

    def getPlayerDirection(self):
        return self.direction