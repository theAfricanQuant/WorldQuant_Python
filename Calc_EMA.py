# -*- coding: utf-8 -*-
def ExponentialMovingAverage(alpha, prices):
    ema = [prices[0]]
    ema.extend(
        round(ema[x] + alpha * (prices[x] - ema[x]), 2)
        for x in range(0, len(prices))
    )
    return ema