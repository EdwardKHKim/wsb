# r/wallstreetbets Ticker Price Correlation
## Overview 

## Dependencies
- [Pandas](https://pandas.pydata.org/)
- [Praw](https://praw.readthedocs.io/en/latest/#)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Alpha Vantage](https://www.alphavantage.co/)

## Reddit Application API
```
reddit_application = praw.Reddit(client_id='', 
                         client_secret='', 
                         user_agent='', 
                         username='', 
                         password='')
```

## Alpha Vantage API
```
config = {
    "alpha_vantage": {
        "key": "", 
        "symbol": "WISH", 
        "outputsize": "compact", 
        "key_adjusted_close": "5. adjusted close",
    }, 

    ...
}

```

## TODO
- Sentiment analysis 
