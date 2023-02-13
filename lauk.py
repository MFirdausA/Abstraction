class ikan:
    def __init__(var, q):
        var.quest = q
        var.Jaw = []
        var.isi = []
        var.nilai = 0

    def dandy(self):
        if self.quest == "M":
            print("_ _ _ _ _")
            self.isi =  [int(x)for x in input("jawaban: ").split()]
            print("Jawaban yang benar:" , self.Jaw)
            print("skor:", self.nilai)
        else:
            print("Main aja")

    def malvin(self):
        import random

        x = [1, 2, 3, 4, 5]
        v = ["a", "b", "c", "d"]

        for i in range(len(x)):
            k= random.choice(x)
            self.Jaw.append(k)
            x.remove(k)

    def skor(self):
        if self.Jaw[0] == self.isi:
            self.nilai += 20
        elif self.Jaw[1] == self.isi[1]:
            self.nilai += 20
        elif self.Jaw[2] == self.isi[2]:
            self.nilai += 20
        elif self.Jaw[3] == self.isi[3]:
            self.nilai += 20
        elif self.Jaw[4] == self.isi[4]:
            self.nilai += 20

def output():
    print("selamat datang")
    q = ikan(input("Masukan [M] jika sudah siap bermain "))
    q.dandy()

if __name__ == "__main__":
    while True:
        output()
