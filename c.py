from b import B


class C(B):
    def __init__(self, terka="default_terka", mc="default_mc", pyt='default_pyt'):
        super().__init__(terka, mc, pyt)

    def oooo(self):
        print("oooo in class C")

    def ooooo(self):
        print("ooooo in class C")
