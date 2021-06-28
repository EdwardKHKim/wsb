from pandas.tseries import frequencies
import praw
import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from matplotlib.pyplot import figure 

from alpha_vantage.timeseries import TimeSeries

reddit_application = praw.Reddit(client_id='', 
                         client_secret='', 
                         user_agent='', 
                         username='', 
                         password='')

subreddit = reddit_application.subreddit('wallstreetbets')

with open('nasdaqtraded.txt') as f: 
    lines = f.readlines() 

companies = lines[1:]
nasdaq_symbols = {}
wsb_symbols = {}

for c in companies:
    symbol = c[2:c.find('|',2)]
    nasdaq_symbols[symbol] = 1 

regex = r'\b([A-Z]+)\b'

for post in subreddit.top('week'):
    strings = [post.title]
    post.comments.replace_more(limit=0)

    for comment in post.comments.list():
        strings.append(comment.body)

    for s in strings:
        for phrase in re.findall(regex, s):
            if phrase in nasdaq_symbols:
                if phrase not in wsb_symbols:
                    wsb_symbols[phrase] = 1
                else:
                    wsb_symbols[phrase] += 1

series = pd.Series(wsb_symbols).sort_values(ascending = False)
print(series[:25])

stocks = (series[:25].keys())
y_pos = np.arange(len(stocks))
frequency = list(series[:25].values)

plt.bar(y_pos, frequency, align='center', alpha=0.5)
plt.xticks(y_pos, stocks)
plt.ylabel('Frequency')
plt.xlabel('Stock Symbol')
plt.title('r/wallstreetbets Stock Frequency - Weekly')

plt.show()


config = {
    "alpha_vantage": {
        "key": "", 
        "symbol": "WISH", 
        "outputsize": "compact", 
        "key_adjusted_close": "5. adjusted close",
    }, 

    "data": {
        "window_size": 20,
    }, 

    "plots": {
        "xticks_interval": 1, 
        "color_actual": "#001f3f",
    }
}

def download_data(config):
    ts = TimeSeries(key=config["alpha_vantage"]["key"])
    data = ts.get_daily_adjusted(config["alpha_vantage"]["symbol"], outputsize=config["alpha_vantage"]["outputsize"])

    data_date = [date for date in data.keys()]
    data_date.reverse()

    data_close_price = [float(data[date][config["alpha_vantage"]["key_adjusted_close"]]) for date in data.keys()]
    data_close_price.reverse()
    data_close_price = np.array(data_close_price)

    num_data_points = len(data_date)
    display_date_range = "from " + data_date[0] + " to " + data_date[num_data_points-1]
    print("Number data points", num_data_points, display_date_range)

    return data_date, data_close_price, num_data_points, display_date_range

data_date, data_close_price, num_data_points, display_date_range = download_data(config)

fig = figure(figsize=(25, 5), dpi=80)
fig.patch.set_facecolor((1.0, 1.0, 1.0))
plt.plot(data_date, data_close_price, color=config["plots"]["color_actual"])
xticks = [data_date[i] if ((i%config["plots"]["xticks_interval"]==0 and (num_data_points-i) > config["plots"]["xticks_interval"]) or i==num_data_points-1) else None for i in range(num_data_points)]
x = np.arange(0,len(xticks))
plt.xticks(x, xticks, rotation='vertical')
plt.title("Daily close price for " + config["alpha_vantage"]["symbol"] + ", " + display_date_range)
plt.grid(b=None, which='major', axis='y', linestyle='--')
plt.show()