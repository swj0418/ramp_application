# ramp_application

## show January 31's rolling 3 day average of total transaction amount processed per day
### Solution
First, we are dealing with time-series data, so we need to sort the transactions by time.

    1. Sort the transaction list
    
The data can include multiple transactions per day. Because the question asks to compute a 3 day average of
"total" transactions,

    2. first consolidate transactions
    
    3. simply the transaction time by removing time of day.
    
Lastly, we compute 3-day average using a sliding window.

    4. Moving average
