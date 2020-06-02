from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()#mouse de panda
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

game = Game()
game.run()

# (all display modules loaded.)
# :gobj(error): Texture::read() - couldn't read: texture/panda_chan_c.png
# :gobj(error): Unable to find texture "texture/panda_chan_c.png" on model-path /home/okadath/Desktop/python/pandas3d/p/ReferenceCode/Lesson2:/home/okadath/.local/share/virtualenvs/pandas3d-JRTpDtiG/lib/python3.6/site-packages/panda3d/etc/..:/home/okadath/.local/share/virtualenvs/pandas3d-JRTpDtiG/lib/python3.6/site-packages/panda3d/etc/../models
# :gobj(error): Texture::read() - couldn't read: texture/panda_chan_ng.png
# :gobj(error): Unable to find texture "texture/panda_chan_ng.png" on model-path /home/okadath/Desktop/python/pandas3d/p/ReferenceCode/Lesson2:/home/okadath/.local/share/virtualenvs/pandas3d-JRTpDtiG/lib/python3.6/site-packages/panda3d/etc/..:/home/okadath/.local/share/virtualenvs/pandas3d-JRTpDtiG/lib/python3.6/site-packages/panda3d/etc/../models

# There is a caveat here: While models can be loaded and allowed to fall out of scope, Actors will not animate properly if this happens. Keep a reference to your Actors as long as you’re using them!
