class Rubl:
    def konvert(self, summa_rub, kurs = 6.1):
        self.summa_rub = summa_rub
        self.kurs = kurs
        result = summa_rub / kurs
        return result