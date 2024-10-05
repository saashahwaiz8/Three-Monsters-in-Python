from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        mace.active()
    else:
        mace.passive()

class Ground(Entity):
    def __init__(self):
        super().__init__(
            scale = Vec3(1000,1,1000),
            texture = 'Floor.jpg',
            collider = 'mesh',
            model = 'plane'
        )

class Earth(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model ='sphere',
            scale = Vec3(1500),
            texture = 'Sky.jfif', 
            double_sided = True
        )
            
class Mace(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2, 0.3),
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.4),
            texture = 'Mace.png'
        )

    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.4, -0.4)

class Enemy1(Entity):
    def __init__(self, player):
        super().__init__(
            scale=Vec3(2, 6, 1.5),
            model='cube',
            texture='Huggy Wuggy.jfif',
            position=Vec3(55, 0, 0)
        )
    
        self.add_script(SmoothFollow(target=player, offset=[0, 1, 0], speed=0.2))

class Enemy2(Entity):
    def __init__(self, player):
        super().__init__(
            scale = Vec3(2, 6, 1.5),
            model = 'cube',
            texture = 'Box.jfif',
            position = Vec3(100, 0, 0)
        )

class Enemy3(Entity):
    def __init__(self, player):
        super().__init__(
            scale = Vec3(2, 6, 1.5),
            model = 'cube',
            texture = 'Catnap.jfif',
            position = Vec3(100, 0, 0)
        )
        
app = Ursina()
Sky() 
window.fullscreen = True
player = FirstPersonController()
player.position = (0, 15, 0)

Ground()
Earth()

mace = Mace()
enemy1 = Enemy1(player)
enemy2 = Enemy2(player)
enemy = Enemy3(player)

app.run()
