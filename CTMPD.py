# Charity Through Marginal Price Discrimination
# http://vitalik.ca/jekyll/general/2017/03/11/a_note_on_charity.html

# TODO: since the disposition of the population being modeled is the key driver of the outcome:
### create a function to easily create new populations
### create a function to easily test and compare all those populations to each other

# THEN: 
# model multiple populations and merchants interacting over iterated games

# If anyone reads this, sorry about the abbreviations. I'm on a very small screen ¯\_(ツ)_/¯
# As this gets updated I'll try to make it more user friendly :) 



# Imports
import numpy as np


# Global Game Variables
ps = 1000  # population size
# rUniPopR and rNormPopSD do not control the same parameters in each population, but they behave similarly within the range of 1 or 2
rUniPopR = 2 # random uniform population range
rNormPopSD = 2  # random normal population standard deviation
au = -2 # action utility
ppc = 7  # product production cost
rpp = 10  # regular product price
epochs = 5  # range to test
pi = 0.01  # rate of price increase as a % of original price
pd = 0.02  # rate of price decrease as a % of original price
# value prop / selling point: for every $1 you give, a person (ideally a beneficial member of society or those in need) receives $2 of value back. It's like Tom's Shoes, but for everything. 


# Create Random Uniformly Distributed Population
# - product utility range based around rpp
# - action utility range based around au
rUniPop = []
for i in range(ps):
  rUniPop.append([])
rUniPopPU = np.random.uniform(rpp - (rpp*rUniPopR),rpp + (rpp*rUniPopR),ps)
rUniPopCounter = 0
for p in rUniPop:
  p.append(rUniPopPU[rUniPopCounter])
  rUniPopCounter += 1
rUniPopAU = np.random.uniform(au - (au*rUniPopR), au + (au*rUniPopR),ps)
rUniPopCounter2 = 0
for p in rUniPop:
  p.append(rUniPopAU[rUniPopCounter2])
  rUniPopCounter2 += 1
rUniPop_sorted_by_au = sorted(rUniPop, key=lambda f: f[1])
#print('\nrUniPop_sorted_by_au:\n',rUniPop_sorted_by_au,'\n')

# Create Random Normally Distributed Population
# - product utility normally distributed around rpp
# - action utility normally distributed around au
rNormPop = []
for i in range(ps):
  rNormPop.append([])
rNormPopPU = np.random.normal(rpp, rNormPopSD, ps)
rNormPopCounter = 0
for p in rNormPop:
  p.append(rNormPopPU[rNormPopCounter])
  rNormPopCounter += 1
rNormPopAU = np.random.normal(au, rNormPopSD, ps)
rNormPopCounter2 = 0
for p in rNormPop:
  p.append(rNormPopAU[rNormPopCounter2])
  rNormPopCounter2 += 1
rNormPop_sorted_by_au = sorted(rNormPop, key=lambda f: f[1])
#print('\nrNormPop_sorted_by_au:\n',rNormPop_sorted_by_au, '\n')


# Function To Model Profits/Costs and Actions
def PCandA(p, ppc, rpp, ip):
  # p: a population of players
  # ppc: product production cost
  # ip: incentivized price
  # rpp: regular price

  # init important variables
  actions = 0
  purchases = 0
  revenue = 0

  # check the utility of a product (pu: product utility) and utility of taking an action (au: action utility) for each member of a population
  for (pu, au) in p:
    # utility of doing nothing
    udn = 0
    # utility of purchase
    up = pu - rpp
    # utility of action
    ua = au
    # utility of action and purchase
    uap = au + pu - ip
    # determine action with max utility
    u_max = max(udn, up, ua, uap)
    # log actions taken
    if u_max in (ua, uap):
      actions += 1
    if u_max in (up, uap):
      purchases += 1
      revenue += ip if uap == u_max else rpp

  # determine profit
  profit = revenue - (purchases*ppc)
  return profit, actions


# Run Model with Random Uniformily Distributed Population
# - ru: random uniform
print('\n\n\nRandom Uniformly Distributed Population')
# Unincentivized
# rurp: ru regular profit, ruatr: ru actions taken regular
rurp, ruatr = PCandA(rUniPop, ppc, rpp, rpp)
# Incentivized
for i in range(epochs):
  # to avoid division by zero
  i += 1
  # ruip: ru incentivized profit, ruati: ru actions taken incentivized
  ruip, ruati = PCandA(rUniPop, ppc, rpp + i*(rpp*pi), rpp - i*(rpp*pi))
  # ruia: ru increased actions
  ruia = ruati - ruatr
  # rucoi: ru cost of incentives
  rucoi = rurp - ruip
  # rucodi: ru cost of direct incentives
  rucodi = (rUniPop_sorted_by_au[-ruatr][1] - rUniPop_sorted_by_au[-ruati][1])*ruati
  #ruvdpodi = ru value per dollar of discount incentives
  ruvdpodi = rucodi / rucoi
  print('\nAt Prices (%.2f, %.2f)' % (rpp + i*(rpp*pi), rpp + -i*(rpp*pd)))
  print('increased actions: %.2f' % (ruia))
  print('cost of incentives: %.2f' % (rucoi))
  print('cost of direct incentivization: %.2f' % (rucodi))
  print('value per dollar of discount incentives: %.2f' % (ruvdpodi))

# Run Model with Normally Distributed Population
# - nd: normally distributed
print('\n\n\nRandom Normally Distributed Population')
# Unincentivized
# ndrp: nd regular profit, ndatr: nd actions taken regular
ndrp, ndatr = PCandA(rNormPop, ppc, rpp, rpp)
# Incentivized
for i in range(epochs):
  # to avoid division by zero
  i += 1
  # ndip: nd incentivized profit, ndati: nd actions taken incentivized
  ndip, ndati = PCandA(rNormPop, ppc, rpp + i*(rpp*pi), rpp + -i*(rpp*pd))
  # ndia: nd increased actions
  ndia = ndati - ndatr
  # ndcoi: nd cost of incentives
  ndcoi = ndrp - ndip
  # ndcodi: nd cost of direct incentives
  ndcodi = ndati * (rNormPop_sorted_by_au[-ndatr][1] - rNormPop_sorted_by_au[-ndati][1])
  #ndvdpodi = nd value per dollar of discount incentives
  ndvdpodi = ndcodi / ndcoi
  print('\nAt Prices (%.2f, %.2f)' % (rpp + i*(rpp*pi), rpp + -i*(rpp*pd)))
  print('increased actions: %.2f' % (ndia))
  print('cost of incentives: %.2f' % (ndcoi))
  print('cost of direct incentivization: %.2f' % (ndcodi))
  print('value per dollar of discount incentives: %.2f' % (ndvdpodi))
