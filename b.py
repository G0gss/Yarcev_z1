from a import A


class B(A):
    def __init__(self, terka, mc, pyt):
        super().__init__(terka, mc)
        self.pyt = pyt

    def ooo(self):
        print("ooo in class B")
