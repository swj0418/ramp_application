# ramp_application

## show January 31's rolling 3 day average of total transaction amount processed per day
### Solution
First, we are dealing with time-series data, so we need to sort the transactions by time.
    
The data can include multiple transactions per day. Because the question asks to compute a 3 day average of
"total" transactions,
    1. first consolidate transactions
    2. simply the transaction time by removing time of day.
    
Lastly, we compute 3-day average using a sliding window.
