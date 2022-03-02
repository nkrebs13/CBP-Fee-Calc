class Trade:
    def __init__(self, trade_id, product, created_at, fee, fee_unit):
        self.trade_id = trade_id
        self.product = product
        self.created_at = created_at
        self.fee = fee
        self.fee_unit = fee_unit

    def printMe(self):
        print("Trade(" + self.trade_id + ", " + self.fee + " " + self.fee_unit + ")")
