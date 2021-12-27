class Dollar:
    def konvert(self, summa_usd, kurs = 438):
        self.summa_usd = summa_usd
        self.kurs = kurs
        result = summa_usd / kurs
        return result