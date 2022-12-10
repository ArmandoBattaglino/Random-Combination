"""
Coefficiente binomiale
"""
def possible_comb(n,k):
  combos = fatt(n)/(fatt(n-k)*fatt(k))
  return combos

def possible_comb_trin(n,k,h):
  combos = fatt(n)/(fatt(h)*fatt(k)*fatt(n-k-h))
  return combos

"""
Fattoriale
"""
def fatt(n):
  numbers = [x+1 for x in range(n)]

  temp = 1
  for x in numbers:
    temp *= x

  return temp
