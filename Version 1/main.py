from ursina import window
import intelligence, engine
from ursina import *

# print("==============================")
# intelligence.ar_ge()
# print("==============================")
#for i in range(100):
#    print(engine.s_rand(i))
# ======================================

app = Ursina()
EditorCamera()
Sky(texture = load_texture('Texture/sky.png'))

ground1 = Entity(model='plane', texture=load_texture('Texture/ground2.png'), collider='mesh', scale=(100, 1, 100), position=(0, 0, 0))
ground2 = Entity(model='plane', texture=load_texture('Texture/ground2.png'), collider='mesh', scale=(100, 1, 100), position=(100, 0, 100))
ground3 = Entity(model='plane', texture=load_texture('Texture/ground2.png'), collider='mesh', scale=(100, 1, 100), position=(0, 0, 100))
ground4 = Entity(model='plane', texture=load_texture('Texture/ground2.png'), collider='mesh', scale=(100, 1, 100), position=(100, 0, 0))

character1 = Entity(model='cube', texture=load_texture('Texture/cell.png'), scale=(1, 0.2, 1), position=(0, 0, 0))
character2 = Entity(model='cube', texture=load_texture('Texture/cell.png'), scale=(1, 0.2, 1), position=(50, 0, 0))
character3 = Entity(model='cube', texture=load_texture('Texture/cell.png'), scale=(1, 0.2, 1), position=(50, 0, 50))
character4 = Entity(model='cube', texture=load_texture('Texture/cell.png'), scale=(1, 0.2, 1), position=(25, 0, 25))

text = Text(text='Energy of Characters', position=window.top_right + Vec2(-0.03, -0.05), origin=(1, 1), scale=1, color=color.white)
text1 = Text(text='Value1: 0', position=window.top_right + Vec2(-0.1, -0.1), origin=(1, 1), scale=1, color=color.white)
text2 = Text(text='Value2: 0', position=window.top_right + Vec2(-0.1, -0.15), origin=(1, 1), scale=1, color=color.white)
text3 = Text(text='Value3: 0', position=window.top_right + Vec2(-0.1, -0.2), origin=(1, 1), scale=1, color=color.white)
text4 = Text(text='Value4: 0', position=window.top_right + Vec2(-0.1, -0.25), origin=(1, 1), scale=1, color=color.white)

PointLight(position=(0, 10, 0), y = 50 ,color=color.white)
light = 120

def update():
    def update_character(character, x):
        if engine.s_light(light, 0, 0, character.x, character.z) >= 0.5:
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
        text2.text = 'C2: {:.2f}'.format(engine.s_light(light, 0, 0, character2.x, character2.z))
        text3.text = 'C3: {:.2f}'.format(engine.s_light(light, 0, 0, character3.x, character3.z))
        text4.text = 'C4: {:.2f}'.format(engine.s_light(light, 0, 0, character4.x, character4.z))

    x = time.localtime().tm_sec

    update_character(character1, engine.Randomise(x).result)
    update_character(character2, engine.Randomise((x + 2) % 60).result)
    update_character(character3, engine.Randomise((x + 3) % 60).result)
    update_character(character4, engine.Randomise((x + 4) % 60).result)

app.run()
