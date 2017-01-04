#coding:utf-8
import datetime
from random import gauss
from math import exp, sqrt
import math

def generate_asset_price(S,v,r,T):
    return S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))

def call_payoff(S_T,K):
    return max(0.0,S_T-K)

S = 857.29 # underlying price
v = 0.1076 # vol of 20.76%  // hacim artış varsayımı
r = 0.0068 # rate of 0.14% //risksiz faiz oranı sabit US Dollar LIBOR interest rate
T = (datetime.date(2013,9,21) - datetime.date(2013,9,3)).days / 365.0
K = 771. #strike
simulations = 90002
payoffs = []
discount_factor = math.exp(-r * T)

for i in range(simulations):
    S_T = generate_asset_price(S,v,r,T)
    payoffs.append(call_payoff(S_T, K))

price = discount_factor * (sum(payoffs) / float(simulations))
print ('Price: %.4f' % price)