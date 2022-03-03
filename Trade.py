class Trade:
    def __init__(self, trade_id, product, created_at, size, price, fee, fee_unit):
        self.trade_id = trade_id
        self.product = product
        self.created_at = created_at
        self.size = float(size)
        self.price = float(price)
        self.fee = float(fee)
        self.fee_unit = fee_unit
        self.volume = self.price * self.size

    def printMe(self):
        print("Trade(" + self.trade_id + ", " + self.fee + " " + self.fee_unit + ")")
