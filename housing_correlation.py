from numpy import corrcoef
import pandas
import sys

frame = pandas.read_csv(sys.argv[1], sep=',')
lotArea, poolArea, yrSold, salePrice = frame["LotArea"], frame["PoolArea"], frame["YrSold"], frame["SalePrice"]
print(corrcoef([lotArea, poolArea, yrSold, salePrice])[1,0])
