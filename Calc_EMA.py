# -*- coding: utf-8 -*-
def ExponentialMovingAverage(alpha, prices):
    ema = []
    ema.append(prices[0])
    for x in range(0, len(prices)):
        ema.append(round(ema[x] + alpha * (prices[x] - ema[x]),2))
    return ema