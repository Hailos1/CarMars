init:
    $ flag = 1
    $ FatherIsDead = True
    image Impius : 
        'Impius.png'
        zoom 1.0
        linear -10.0 xzoom 1.0 yzoom 1.0
    image Mars:
        'Mars.png'
        zoom 0.2
        linear 1.0 xzoom -1.0 yzoom 1.0
    default persistent.bg_parallax = True
    define parallax_bg_size = (2200, 1237) # needs to be bigger than the screen size (1920, 1080)
    image bg black: 
        'black.jpg'
        xysize parallax_bg_size

    # Определение персонажей игры.
    define mars = Character('Марс', color="#440078", image='Mars')
    define impius = Character('Импиус', color="#ff0000", image='Impius')
    define benignus = Character('Бунигнус', color="#005ac2")
    define marte = Character('Марта', color="#ff7bd3")
    define kletus = Character('Клетус', color="#78ffb5")

    image bg kepler186: 
        'Kepler186f.jpg'    
        xysize parallax_bg_size
    image containersBG = 'склад.jpg'