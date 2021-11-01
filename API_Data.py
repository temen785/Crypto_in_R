def coin_data (coin ,Interval, start_str, pair='USDT'):
    import pandas as pd
    from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
    from binance_keys import  API_key, Secret_Key
    from datetime import datetime
    import time
    Client = Client(API_key, Secret_Key)
    
    if (Interval == '1m'):
        interval = Client.KLINE_INTERVAL_1MINUTE
    elif (Interval == '3m'):
        interval = Client.KLINE_INTERVAL_3MINUTE
    elif (Interval == '5m'):
        interval = Client.KLINE_INTERVAL_5MINUTE
    elif (Interval =='15m'):
        interval = Client.KLINE_INTERVAL_15MINUTE 
    elif (Interval == '30m') :
        interval = Client.KLINE_INTERVAL_30MINUTE
    elif (Interval == '1h') :   
        interval = Client.KLINE_INTERVAL_1HOUR
    elif (Interval == '2h') :
        interval = Client.KLINE_INTERVAL_2HOUR
    elif (Interval == '4h') :    
        interval = Client.KLINE_INTERVAL_4HOUR
    elif (Interval == '6h') :
        interval = Client.KLINE_INTERVAL_6HOUR
    elif (Interval == '8h') :
        interval = Client.KLINE_INTERVAL_8HOUR 
    elif (Interval == '12h') :
        interval = Client.KLINE_INTERVAL_12HOUR
    elif (Interval == '1d') :
        interval =  Client.KLINE_INTERVAL_1DAY  
    elif (Interval == '3d') :
        interval = Client.KLINE_INTERVAL_3DAY
    elif (Interval == '1w') :
        interval = Client.KLINE_INTERVAL_1WEEK
    elif (Interval == '1M') :
        interval = Client.KLINE_INTERVAL_1MONTH 
        
    Klines =Client.get_historical_klines(symbol= f'{coin}' f'{pair}', interval=interval , start_str = start_str)
    cols = ['OpenTime',
            f'{coin}' '-' f'{pair}' '_Open',
            f'{coin}' '-' f'{pair}' '_High',
            f'{coin}' '-' f'{pair}' '_Low',
            f'{coin}' '-' f'{pair}' '_Close',
            f'{coin}' '-' f'{pair}' '_volume',
            'CloseTime',
            f'{coin}-QuoteAssetVolume',
            f'{coin}-NumberOfTrades',
            f'{coin}-TBBAV',
            f'{coin}-TBQAV',
            f'{coin}-ignore']

    coin_df = pd.DataFrame(Klines,columns=cols)
    all_coins_df = coin_df
    all_coins_df['OpenTime'] = [datetime.fromtimestamp(ts / 1000) for ts in all_coins_df['OpenTime']]
    all_coins_df['CloseTime'] = [datetime.fromtimestamp(ts / 1000) for ts in all_coins_df['CloseTime']]

    for col in all_coins_df.columns:
        if not 'Time' in col:
            all_coins_df[col] = all_coins_df[col].astype(float)
    return (all_coins_df)


