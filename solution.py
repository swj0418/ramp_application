import os
from datetime import datetime


transactions = [
    {"transaction_time": "2021-01-16 00:05:54", "transaction_amount": 25.05},
    {"transaction_time": "2021-01-07 20:53:04", "transaction_amount": 124.00},
    {"transaction_time": "2021-01-18 22:55:37", "transaction_amount": 66.58},
    {"transaction_time": "2021-01-21 00:36:57", "transaction_amount": 9.99},
    {"transaction_time": "2021-01-19 06:31:10", "transaction_amount": 22.27},
    {"transaction_time": "2021-01-10 01:24:04", "transaction_amount": 576.76},
    {"transaction_time": "2021-01-04 00:07:27", "transaction_amount": 49.91},
    {"transaction_time": "2021-01-25 20:36:17", "transaction_amount": 14.11},
    {"transaction_time": "2021-01-08 21:11:16", "transaction_amount": 112.21},
    {"transaction_time": "2021-01-07 00:06:21", "transaction_amount": 331.80},
    {"transaction_time": "2021-01-18 09:30:10", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-22 20:30:14", "transaction_amount": 130.72},
    {"transaction_time": "2021-01-18 00:06:21", "transaction_amount": 91.53},
    {"transaction_time": "2021-01-01 09:29:56", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-13 20:50:02", "transaction_amount": 33.04},
    {"transaction_time": "2021-01-05 00:06:15", "transaction_amount": 142.30},
    {"transaction_time": "2021-01-09 01:02:40", "transaction_amount": 15.00},
    {"transaction_time": "2021-01-12 05:49:02", "transaction_amount": 28.25},
    {"transaction_time": "2021-01-03 00:03:22", "transaction_amount": 14.69},
    {"transaction_time": "2021-01-05 00:49:45", "transaction_amount": 93.25},
    {"transaction_time": "2021-01-12 20:38:30", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-31 00:09:01", "transaction_amount": 23.10},
    {"transaction_time": "2021-01-11 10:56:16", "transaction_amount": 75.64},
    {"transaction_time": "2021-01-30 00:04:01", "transaction_amount": 6.75},
    {"transaction_time": "2021-01-04 11:35:53", "transaction_amount": 4.99},
    {"transaction_time": "2021-01-29 05:39:47", "transaction_amount": 33.73},
    {"transaction_time": "2021-01-08 06:37:49", "transaction_amount": 143.12},
    {"transaction_time": "2021-01-07 00:48:07", "transaction_amount": 20.00},
    {"transaction_time": "2021-01-24 11:01:21", "transaction_amount": 1058.40},
    {"transaction_time": "2021-01-21 04:41:26", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-05 21:34:58", "transaction_amount": 100.00},
    {"transaction_time": "2021-01-06 00:48:00", "transaction_amount": 362.91},
    {"transaction_time": "2021-01-13 00:51:59", "transaction_amount": 19.24},
    {"transaction_time": "2021-01-17 00:10:53", "transaction_amount": 32.46},
    {"transaction_time": "2021-01-20 01:04:34", "transaction_amount": 32.76},
    {"transaction_time": "2021-01-30 07:55:26", "transaction_amount": 59.37},
    {"transaction_time": "2021-01-03 11:03:52", "transaction_amount": 36.37},
    {"transaction_time": "2021-01-21 19:33:01", "transaction_amount": 12.99},
    {"transaction_time": "2021-01-30 00:58:25", "transaction_amount": 400.00},
    {"transaction_time": "2021-01-14 06:14:03", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-26 00:02:21", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-01 00:12:28", "transaction_amount": 5000.00},
    {"transaction_time": "2021-01-26 04:45:44", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-23 04:31:41", "transaction_amount": 623.72},
    {"transaction_time": "2021-01-25 08:48:28", "transaction_amount": 33.05},
    {"transaction_time": "2021-01-18 01:20:23", "transaction_amount": 48.75},
    {"transaction_time": "2021-01-22 00:41:55", "transaction_amount": 47.00},
    {"transaction_time": "2021-01-28 00:05:20", "transaction_amount": 35.00},
    {"transaction_time": "2021-01-29 00:06:33", "transaction_amount": 1450.00},
    {"transaction_time": "2021-01-16 00:44:31", "transaction_amount": 82.38},
    {"transaction_time": "2021-01-31 13:00:35", "transaction_amount": 19.00},
    {"transaction_time": "2021-01-11 01:18:30", "transaction_amount": 2130.54},
    {"transaction_time": "2021-01-20 05:44:23", "transaction_amount": 13.02},
    {"transaction_time": "2021-01-27 19:50:22", "transaction_amount": 150.00},
    {"transaction_time": "2021-01-15 00:04:12", "transaction_amount": 641.37},
    {"transaction_time": "2021-01-19 01:10:40", "transaction_amount": 235.44},
    {"transaction_time": "2021-01-27 00:37:59", "transaction_amount": 216.99},
    {"transaction_time": "2021-01-27 04:53:20", "transaction_amount": 54.35},
    {"transaction_time": "2021-01-19 00:04:03", "transaction_amount": 99.95},
    {"transaction_time": "2021-01-06 20:49:50", "transaction_amount": 57.08},
    {"transaction_time": "2021-01-17 12:39:03", "transaction_amount": 22.75},
    {"transaction_time": "2021-01-05 06:24:32", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-31 01:56:35", "transaction_amount": 17.33},
    {"transaction_time": "2021-01-11 21:35:49", "transaction_amount": 10.66},
    {"transaction_time": "2021-01-13 06:38:51", "transaction_amount": 9.99},
    {"transaction_time": "2021-01-15 00:53:48", "transaction_amount": 450.00},
    {"transaction_time": "2021-01-28 00:39:16", "transaction_amount": 27.92},
    {"transaction_time": "2021-01-17 01:21:03", "transaction_amount": 13.61},
    {"transaction_time": "2021-01-02 11:07:27", "transaction_amount": 84.31},
    {"transaction_time": "2021-01-19 19:55:26", "transaction_amount": 15.10},
    {"transaction_time": "2021-01-24 01:27:27", "transaction_amount": 47.90},
    {"transaction_time": "2021-01-12 00:48:20", "transaction_amount": 8413.94},
    {"transaction_time": "2021-01-09 00:02:48", "transaction_amount": 118.49},
    {"transaction_time": "2021-01-15 06:18:10", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-22 00:05:13", "transaction_amount": 23.04},
    {"transaction_time": "2021-01-03 01:32:21", "transaction_amount": 3.00},
    {"transaction_time": "2021-01-14 00:04:24", "transaction_amount": 9.99},
    {"transaction_time": "2021-01-22 05:29:08", "transaction_amount": 326.24},
    {"transaction_time": "2021-01-10 11:05:01", "transaction_amount": 43.55},
    {"transaction_time": "2021-01-02 01:14:35", "transaction_amount": 513.00},
    {"transaction_time": "2021-01-20 00:03:47", "transaction_amount": 14.23},
    {"transaction_time": "2021-01-13 00:03:52", "transaction_amount": 429.11},
    {"transaction_time": "2021-01-28 04:39:11", "transaction_amount": 37.17},
    {"transaction_time": "2021-01-26 00:40:51", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-04 21:14:08", "transaction_amount": 889.46},
    {"transaction_time": "2021-01-21 23:53:40", "transaction_amount": 43.99},
    {"transaction_time": "2021-01-24 00:06:29", "transaction_amount": 59.00},
    {"transaction_time": "2021-01-08 00:04:24", "transaction_amount": 60.46},
    {"transaction_time": "2021-01-06 06:49:28", "transaction_amount": 16.41},
    {"transaction_time": "2021-01-14 21:09:48", "transaction_amount": 100.00},
    {"transaction_time": "2021-01-04 01:45:23", "transaction_amount": 340.80},
    {"transaction_time": "2021-01-20 19:46:38", "transaction_amount": 90.00},
    {"transaction_time": "2021-01-16 06:35:34", "transaction_amount": 29.00},
    {"transaction_time": "2021-01-26 19:52:38", "transaction_amount": 704.47},
    {"transaction_time": "2021-01-09 10:44:29", "transaction_amount": 900.00},
    {"transaction_time": "2021-01-21 00:07:15", "transaction_amount": 59.00},
    {"transaction_time": "2021-01-29 00:43:11", "transaction_amount": 17.82},
    {"transaction_time": "2021-01-25 00:04:42", "transaction_amount": 119.95},
    {"transaction_time": "2021-01-23 00:35:56", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-27 00:01:48", "transaction_amount": 50.00},
    {"transaction_time": "2021-01-28 19:44:55", "transaction_amount": 8874.32},
    {"transaction_time": "2021-01-29 20:37:37", "transaction_amount": 19.35},
    {"transaction_time": "2021-01-06 00:04:15", "transaction_amount": 8.20},
    {"transaction_time": "2021-01-14 00:40:59", "transaction_amount": 2.84},
    {"transaction_time": "2021-01-12 00:06:22", "transaction_amount": 1516.39},
    {"transaction_time": "2021-01-07 06:31:13", "transaction_amount": 500.00},
    {"transaction_time": "2021-01-10 00:04:58", "transaction_amount": 131.44},
    {"transaction_time": "2021-01-23 00:02:24", "transaction_amount": 103.20},
    {"transaction_time": "2021-01-25 01:21:44", "transaction_amount": 123.84},
    {"transaction_time": "2021-01-11 00:06:39", "transaction_amount": 87.10},
    {"transaction_time": "2021-01-01 02:01:09", "transaction_amount": 518.20},
    {"transaction_time": "2021-01-15 20:55:58", "transaction_amount": 47.72},
    {"transaction_time": "2021-01-02 00:09:43", "transaction_amount": 49.00},
    {"transaction_time": "2021-01-08 00:49:22", "transaction_amount": 31.61}
]


if __name__ == '__main__':
    # show January 31's rolling 3 day average of total transaction amount processed per day
    """
    Solution
        First, we are dealing with time-series data, so we need to sort the transactions by time.
        
        The data can include multiple transactions per day. Because the question asks to compute a 3 day average of
        "total" transactions,
            1. first consolidate transactions
            2. simply the transaction time by removing time of day.
            
        Lastly, we compute 3-day average using a sliding window.
    """

    transactions.sort(key=lambda x: x["transaction_time"])

    volumes = []
    x, y = 0, 1
    while y < len(transactions):
        x_t = str(transactions[x]['transaction_time'])
        y_t = str(transactions[y]['transaction_time'])
        if (datetime.strptime(x_t, '%Y-%m-%d %H:%M:%S').day
                == datetime.strptime(y_t, '%Y-%m-%d %H:%M:%S').day):
            y += 1
        else:  # Consolidate and move on
            volumes.append(sum([v['transaction_amount'] for v in transactions[x: y]]))
            x = y
            y += 1

    # Last 3-day average
    ma = sum(volumes[-3:]) / 3
    print(ma)
