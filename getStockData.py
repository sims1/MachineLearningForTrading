# This file is using historical Data
#
# Real time Data:
#   From Yahoo Finance http://www.jarloo.com/yahoo_finance/
# Historical Data
#   From: http://community.jaspersoft.com/wiki/building-custom-datasource-yahoo-finance-data

import urllib

stocks = ['GOOG']
#dataOption = ['n', 'a', 'b']
dataTitle = ['Trade Date', 'previous close', 'open', 'high', 'low', 'volume']
dataOption = ['d2', 'p', 'o', 'h', 'g', 'v', ]
outputFile = 'output.csv'

def retrieve(stocks, dataOption, outputFile):
    for stockString in stocks:
        url = 'http://ichart.finance.yahoo.com/table.csv?s={0}'.format(stockString)
        urllib.urlretrieve(url, outputFile)


def main():
    # TODO: get the following information from command line
    retrieve(stocks, dataOption, outputFile)

if __name__ == "__main__":
    main()
