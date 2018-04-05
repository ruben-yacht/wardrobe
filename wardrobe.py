from enum import Enum

class Material(Enum):
    WOOD = 1
    GLASS = 2
    CARBON_FIBRE = 3

class Wardrobe():
    def __init__(self, name, material=Material.WOOD):
        if isinstance(material, Material):
            self._material = material
        else:
            raise TypeError("material should be of type Material.")

        self._name = name
        self._opened = False
        self._someone_in = False
        self._broken = False

    def open(self):
        if(not self._broken):
            self._opened = True
            return "wardrobe is now open"
        else:
            return "can't open - the wardrobe is broken!"

    def close(self):
        if(not self._broken):
            self._opened = False
            return "wardrobe is now closed"
        else:
            return "can't close - the wardrobe is broken!"

    def get_in(self):
        if(not self._broken):
            if not self._someone_in:
                if self._opened:
                    self._someone_in = True
                    return "getting into the wardrobe"
                else:
                    return "can't get in; the wardrobe is closed"
            return "there's already someone in the wardrobe"
        else:
            return "can't get in - the wardrobe is broken!"


    def get_out(self):
        if(not self._broken):
            if self._someone_in:
                if self._opened:
                    return "getting out of the wardrobe"
                else:
                    return "wardrobe is closed"
            return "no-one in the wardrobe"
        else:
            return "can't get out - the wardrobe is broken!"

    def kick(self, force):
        if not self._broken:
            if (force > 5):
                if(self._material == Material.WOOD):
                    return "boom - wood everywhere!"
                elif(self._material == Material.GLASS):
                    return "shatter - glass everywhere!"
                elif(self._material == Material.CARBON_FIBRE):
                    return "boom, broken!"
                else:
                    print(self._material)
                    return "unknown material"
            else:
                return "the kick was weak. nothing happened"
        else:


if __name__ == "__main__":
    myWardrobe = Wardrobe("peter the wardrobe", Material.CARBON_FIBRE)
    print(myWardrobe.open())
    print(myWardrobe.get_in())
    print(myWardrobe.get_out())
    print(myWardrobe.close())
    print(myWardrobe.kick(10))
