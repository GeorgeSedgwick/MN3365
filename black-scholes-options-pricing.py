import math
import numpy as np
from scipy.stats import norm

class Black_Scholes(object):
    """
    Black-Scholes European options pricing model
    """
    def __init__(self, S, K, T, r, vol):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.vol = vol
        self.pv_k = self.K / np.exp((self.r * self.T))


    def d1(self):
        return (np.log(self.S / self.K) + (self.r + (self.vol ** 2 / 2)) * self.T) / (self.vol * math.sqrt(self.T))
    
    def d2(self):
        return self.d1() - self.vol * math.sqrt(self.T)
    
    def call_price(self):
        return self.S * norm.cdf(self.d1()) - self.pv_k * norm.cdf(self.d2())

    def put_price(self):
        return -self.S * (1 - norm.cdf(self.d1())) + self.pv_k * (1 - norm.cdf(self.d2()))
    
    


bs = Black_Scholes(S=120, K=100, T=.25, r=.0168, vol=.4)
print(f"Call Price: {bs.call_price()}")
print(f"Put Price: {bs.put_price()}")
