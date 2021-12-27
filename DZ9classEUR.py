class Euro:
    def konvert(self, summa_euro, kurs = 502):
        self.summa_euro = summa_euro
        self.kurs = kurs
        result = summa_euro / kurs
        return result