from ursina import window
import intelligence, engine
from ursina import *

app = Ursina()
EditorCamera()
Sky()

ground1 = Entity(model='plane', texture=load_texture('Texture/ground.png'), collider='mesh', scale=(100, 1, 100), position=(0, 0, 0))

character1 = Entity(model='cube', texture=load_texture('Texture/cell.png'), scale=(1, 0.2, 1), position=(0, 0, 0))
robot1 = Entity(model='cube', texture=load_texture('Texture/robot_2.png'), scale=(1, 0.2, 1), position=(30, 0, 30))

text = Text(text='Energy of Characters', position=window.top_right + Vec2(-0.03, -0.05), origin=(1, 1), scale=1, color=color.white)
text1 = Text(text='Value1: 0', position=window.top_right + Vec2(-0.1, -0.1), origin=(1, 1), scale=1, color=color.white)

PointLight(position=(0, 10, 0), y = 50 ,color=color.white)
light = 120

def update():
    def update_character(character, x, serial_number):
        if engine.s_light(light, 0, 0, character.x, character.z) >= 0.5:
            if 20000 > x > 12000:
                character.x += 3 * time.dt
            if 24000 > x > 20000:
                character.x -= 3 * time.dt
            if 12000 > x > 6000:
                character.z += 3 * time.dt
            if 6000 > x > 0:
                character.z -= 3 * time.dt
        elif serial_number == 1:
            if 20000 > x > 12000:
                character.x += 3 * time.dt
            if 24000 > x > 20000:
                character.x -= 3 * time.dt
            if 12000 > x > 6000:
                character.z += 3 * time.dt
            if 6000 > x > 0:
                character.z -= 3 * time.dt
        else:
            print("Nothing is happening")
        character.z = max(character.z, 0)
        text1.text = 'C1: {:.2f}'.format(engine.s_light(light, 0, 0, character1.x, character1.z))

    x = time.localtime().tm_sec

    update_character(character1, engine.Randomise(x, 0).result, 0)
    update_character(robot1, engine.Randomise((x + 35) % 60, 1).result, 1)

app.run()
