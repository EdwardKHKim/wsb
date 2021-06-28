# r/wallstreetbets Ticker Price Correlation
## Overview 

## Dependencies
- [Pandas](https://pandas.pydata.org/)
- [Praw](https://praw.readthedocs.io/en/latest/#)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Alpha Vantage](https://www.alphavantage.co/)

## Reddit Application API
Change value of ```client_id```, ```client_secret```, ```user_agent```, ```username``` and ```password```.
```
reddit_application = praw.Reddit(client_id='GENERAL API KEY', 
                         client_secret='SECRET API KEY', 
                         user_agent='APPLICATION NAME', 
                         username='REDDIT ACCOUNT USERNAME', 
                         password='REDDIT ACCOUNT PASSWORD')
```

## Alpha Vantage API
Change value of ```key``` and ```symbol```.
```
config = {
    "alpha_vantage": {
        "key": "ALPHA VANTAGE API KEY", 
        "symbol": "STOCK TICKER", 
        "outputsize": "compact", 
        "key_adjusted_close": "5. adjusted close",
    }, 

    ...
}

```

## TODO
- Sentiment analysis 
