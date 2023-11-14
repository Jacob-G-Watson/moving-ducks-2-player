class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    Gap = SpriteKind.create()

def on_up_pressed():
    mySprite.y += -10
    animation.set_action(mySprite, ActionKind.Jumping)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_released():
    
    def on_after():
        animation.set_action(mySprite, ActionKind.Idle)
    timer.after(animationTimer, on_after)
    
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    mySprite.x += -10
    animation.set_action(mySprite, ActionKind.Jumping)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    
    def on_after2():
        animation.set_action(mySprite, ActionKind.Idle)
    timer.after(animationTimer, on_after2)
    
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    
    def on_after3():
        animation.set_action(mySprite, ActionKind.Idle)
    timer.after(animationTimer, on_after3)
    
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def SetUpAnimations():
    global animationTimer, mySprite, anim
    animationTimer = 250
    mySprite = sprites.create(img("""
            . . . . . . . . . . b 5 b . . . 
                    . . . . . . . . . b 5 b . . . . 
                    . . . . . . . . . b c . . . . . 
                    . . . . . . b b b b b b . . . . 
                    . . . . . b b 5 5 5 5 5 b . . . 
                    . . . . b b 5 d 1 f 5 5 d f . . 
                    . . . . b 5 5 1 f f 5 d 4 c . . 
                    . . . . b 5 5 d f b d d 4 4 . . 
                    b d d d b b d 5 5 5 4 4 4 4 4 b 
                    b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                    b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                    c d d c d 5 5 b 5 5 5 5 5 5 b . 
                    c b d d c c b 5 5 5 5 5 5 5 b . 
                    . c d d d d d d 5 5 5 5 5 d b . 
                    . . c b d d d d d 5 5 5 b b . . 
                    . . . c c c c c c c c b b . . .
        """),
        SpriteKind.player)
    anim = animation.create_animation(ActionKind.Jumping, 25)
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . b 5 5 b . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . b b b b b 5 5 5 5 5 5 5 b . . 
                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                . . b d 5 5 b 1 f f 5 4 4 c . . 
                b b d b 5 5 5 d f b 4 4 4 4 b . 
                b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . b b b b b 5 5 5 5 5 5 5 b . . 
                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                . . b d 5 5 b 1 f f 5 4 4 c . . 
                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . . . . b c . . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 5 d f . . 
                . . . . b 5 5 1 f f 5 d 4 c . . 
                . . . . b 5 5 d f b d d 4 4 . . 
                b d d d b b d 5 5 5 4 4 4 4 4 b 
                b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                c d d c d 5 5 b 5 5 5 5 5 5 b . 
                c b d d c c b 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 d 4 c . . 
                . . . . b 5 5 1 f f d d 4 4 4 b 
                . . . . b 5 5 d f b 4 4 4 4 b . 
                . . . b d 5 5 5 5 4 4 4 4 b . . 
                . . b d d 5 5 5 5 5 5 5 5 b . . 
                . b d d d d 5 5 5 5 5 5 5 5 b . 
                b d d d b b b 5 5 5 5 5 5 5 b . 
                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                c b b d 5 d c d 5 5 5 5 5 5 b . 
                . b 5 5 b c d d 5 5 5 5 5 d b . 
                b b c c c d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 d 4 c . . 
                . . . . b 5 5 1 f f d d 4 4 4 b 
                . . . . b 5 5 d f b 4 4 4 4 b . 
                . . . b d 5 5 5 5 4 4 4 4 b . . 
                . b b d d d 5 5 5 5 5 5 5 b . . 
                b d d d b b b 5 5 5 5 5 5 5 b . 
                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                c b b d 5 d c d 5 5 5 5 5 5 b . 
                c b 5 5 b c d d 5 5 5 5 5 5 b . 
                b b c c c d d d 5 5 5 5 5 d b . 
                . . . . c c d d d 5 5 5 b b . . 
                . . . . . . c c c c c b b . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . b 5 b . . . 
                . . . . . . . . . b 5 b . . . . 
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 5 d f . . 
                . . . . b 5 5 1 f f 5 d 4 c . . 
                . . . . b 5 5 d f b d d 4 4 . . 
                . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                b d d d b b d 5 5 4 4 4 4 4 b . 
                b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                c b d c d 5 5 b 5 5 5 5 5 5 b . 
                . c d d c c b d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . . 
                . . . . . . . . . . . . . . . .
    """))
    animation.attach_animation(mySprite, anim)

def on_on_overlap(sprite, otherSprite):
    if otherSprite.right - sprite.left < 2:
        info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Gap, on_on_overlap)

def on_right_pressed():
    mySprite.x += 10
    animation.set_action(mySprite, ActionKind.Jumping)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

def on_up_released():
    
    def on_after4():
        animation.set_action(mySprite, ActionKind.Idle)
    timer.after(animationTimer, on_after4)
    
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    mySprite.y += 10
    animation.set_action(mySprite, ActionKind.Jumping)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

anim: animation.Animation = None
animationTimer = 0
mySprite: Sprite = None
scene.set_background_color(9)
info.set_score(0)
effects.blizzard.start_screen_effect()
SetUpAnimations()
mySprite.set_position(73, 112)

def on_on_update():
    if mySprite.top < 0:
        game.over(True)
    if mySprite.bottom > 120:
        mySprite.y += -10
    elif mySprite.right > 160:
        mySprite.x += -10
    elif mySprite.left < 0:
        mySprite.x += 10
game.on_update(on_on_update)
