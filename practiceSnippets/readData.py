import pandas

# index
def test_run1(inputCsv):
    dataFrame = pandas.read_csv(inputCsv)
    print 'First 5 lines:'
    print dataFrame.head() # head() means top 5 lines
    print 'Last 5 lines:'
    print dataFrame.tail() # head() means top 5 lines
    print 'Last 10 lines:'
    print dataFrame.tail(10) # head() means top 5 lines
    print 'Last index 10 to 20:'
    print dataFrame[10:21]

# get Max
def getMaxClose(inputCsv, symbol):
    dataFrame = pandas.read_csv(inputCsv)
    return dataFrame['Close'].max()

def test_run2(inputCsv):
    for symbol in ['GOOG']:
        print 'max close'
        print symbol, getMaxClose(inputCsv, symbol)

def main():
    #test_run1('output.csv')
    test_run2('output.csv') 


if __name__ == "__main__":
    main()
