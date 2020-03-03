class cats:
    def __init__(self,attitude1,skin1):
        self.attitude = attitude1
        self.skin = skin1

    face = "whiskers"
    legs = 4
    
    mittens = cats("lazy","fur")

    print(getattr(mittens.attitude,mittens.skin))