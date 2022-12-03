class Contestants():
    _player_list = []
    def __init__(self, player_list):
        self._player_list = player_list
        #Begins the instance of two players
        '''Attributes:
        ks=KeyboardService()
        self.direct = Direction()
        self.a = (-1,0)
        self.s = (0,-1)
        self.d = (+1,0)
        self.w = (0,+1)
        self.j = (-1,0)
        self.k = (0,-1)
        self.l = (+1,0)
        self.i = (0,+1)
        self.x = Point.get_x()
        self.y = Point.get_y()
        '''
    def get_players(self):
        return self._player_list

    def execute(self,point):
        if self.direct == self.a:
            self.x -= 1 
        elif self.direct == self.s:
            self.y -= 1
        elif self.direct == self.d:
            self.x += 1
        elif self.direct == self.w:
            self.y += 1
        elif self.direct == self.k:
            self.y -= 1
        elif self.direct == self.l:
            self.x += 1
        elif self.direct == self.i:
            self.y += 1
        elif self.direct == self.j:
            self.x -= 1  