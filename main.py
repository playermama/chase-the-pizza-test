mySprite: Sprite = None
info.change_countdown_by(controller.player2.dx(100))
animation.run_image_animation(mySprite, assets.animation("""
    player
"""), 500, True)
scene.set_background_color(0)
mySprite = sprites.create(assets.image("""
    home
"""), SpriteKind.player)
mySprite.set_position(0, 0)
mySprite2: number = sprites.create(img("""
        333333333333cccc66666...........
            3.......ccc4444444444666........
            3.....cc444444444bb4444466......
            3....cb4444bb4444b5b444444b.....
            3...eb4444b5b44444b44444444b....
            3..ebb44444b4444444444b444446...
            3.eb6bb444444444bb444b5b444446..
            ..e6bb5b44444444b5b444b44bb44e..
            .e66b4b4444444444b4444444b5b44e.
            .e6bb444444444444444444444bb44e.
            eb66b44444bb444444444444444444be
            eb66bb444b5b44444444bb44444444be
            fb666b444bb444444444b5b4444444bf
            fcb666b44444444444444bb444444bcf
            .fbb6666b44444444444444444444bf.
            .efbb66666bb4444444444444444bfe.
            .86fcbb66666bbb44444444444bcc688
            8772effcbbbbbbbbbbbbbbbbcfc22778
            87722222cccccccccccccccc22226678
            f866622222222222222222222276686f
            fef866677766667777776667777fffef
            fbff877768f86777777666776fffffbf
            fbeffeefffeff7766688effeeeefeb6f
            f6bfffeffeeeeeeeeeeeeefeeeeebb6e
            f66ddfffffeeeffeffeeeeeffeedb46e
            .c66ddd4effffffeeeeeffff4ddb46e.
            .fc6b4dddddddddddddddddddb444ee.
            ..ff6bb444444444444444444444ee..
            ....ffbbbb4444444444444444ee....
            ......ffebbbbbb44444444eee......
            .........fffffffcccccee.........
            ................................
    """),
    SpriteKind.player)
mySprite2 = 0