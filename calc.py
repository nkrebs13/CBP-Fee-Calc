import csv
import json
from Trade import Trade

# Read in files
all_trades = []
trade_count = 0
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        trade_id = row[1]
        product = row[2]
        side = row[3]
        created_at = row[4]
        size = row[5]
        unit = row[6]
        price = row[7]
        fee = row[8]
        total = row[9]
        total_unit = row[10]

        all_trades.append(Trade(trade_id, product, created_at, fee, total_unit))
        trade_count += 1

# remove header
all_trades.pop(0)
trade_count -= 1

# Order by trade unit
trades_by_product = {}
for trade in all_trades:
    if trade.fee_unit in trades_by_product:
        trades_by_product[trade.fee_unit] += float(trade.fee)
    else:
        trades_by_product[trade.fee_unit] = float(trade.fee)

trade_products_sorted = sorted(trades_by_product.keys())

print("Total Fees")
for product_key in trade_products_sorted:
    total = str(trades_by_product[product_key])
    print("  " + product_key + " " + total)

print("Total Trades: " + str(trade_count))
