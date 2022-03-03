import csv
import json
from Trade import Trade

# Read in files
all_trades = []
trade_count = 0
with open('fills.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
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

        all_trades.append(Trade(trade_id, product, created_at, size, price, fee, total_unit))
        trade_count += 1

# Order by trade unit
trades_by_product = {}
for trade in all_trades:
    if trade.fee_unit in trades_by_product:
        new_fee = trades_by_product[trade.fee_unit]['fee'] + trade.fee
        new_volume = trades_by_product[trade.fee_unit]['volume'] + trade.volume
        trades_by_product[trade.fee_unit] = {'fee': new_fee, 'volume' : new_volume}
    else:
        trades_by_product[trade.fee_unit] = {'fee': trade.fee, 'volume' : trade.volume}

trade_products_sorted = sorted(trades_by_product.keys())

print("\nTotal Trades: " + str(trade_count))

print("\nTotal Fees")
for product_key in trade_products_sorted:
    total = str(trades_by_product[product_key]['fee'])
    print("  " + product_key + " " + total)

print("\nTotal Volume -> % fee / trade")
for product_key in trade_products_sorted:
    volume = trades_by_product[product_key]['volume']
    fee = trades_by_product[product_key]['fee']
    factor = float(fee / volume) * 100.0
    perc = "{:.2f}".format(factor)
    print("  " + product_key + " " + str(volume) + " -> " + perc + "%")
