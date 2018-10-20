# Quadratic Voting Anti Centralization Gadget
# https://ethresear.ch/t/quadratic-costs-and-collective-payouts-as-anti-centralization-gadget/2429


# Summary

# People pay a fee to vote, and voting fees are redistributed to voters after voting is completed.
# The amount you pay is quadratically proportional to the size of your vote. 
# The amount you receive is linearly proportional to the size of your vote. 

# This means that larger voters pay smaller voters to participate, 
# and even if they try to split their votes into smaller accounts 
# and the entire market converges to an equilibrium of uniformly sized accounts, 
# the best they can do is break even on fees.

# This still doesn't solve the problem that larger token holders would have more votes overall, 
# but it ads an extra incentive for smaller parties to participate in the process. 
# Also, if dishonest behavior results in a node's stake being slashed relative to the % of the network that also acted dishonestly,
# then the larger the network of voting nodes the stronger the incentive to play nice.

# NOTE: the quadradic voting fee mechanism implimented here is NOT the same as was described in the original post. 
# This mechanism assumes that participating voters are staking their entire balance. 
# Also, in the original post I wasn't sure what Xi represents so I created a binary voting system 
# where -1 means no, 0 means not participating, and 1 means yes. 
# This is just a test to get a general mechanism working and better understand 
# how QV fees would work in an iterated setting like block voting. Further upgrades and refinements TBD. 



# Imports
import numpy as np

# Global Game Variables
totalSupply = 1000000
numAccounts = 100
numWhales = 5
numMedAccounts = 15
numSmallAccounts = 80
whalePreMine = (0.4*totalSupply) / numWhales
medAccountsPreMine = (0.4*totalSupply) / numMedAccounts
smallAccountsPreMine = (0.2*totalSupply) / numSmallAccounts
mixingRounds = 100000
txRange = 100
votingFee = 0.8
votingRounds = 10000
printFrequency = votingRounds/10

# Create Randomized Accounts
def createRandomAccounts(totalSupply, 
                        numAccounts, 
                        numWhales,
                        numMedAccounts,
                        numSmallAccounts,
                        whalePreMine,
                        medAccountsPreMine,
                        smallAccountsPreMine, 
                        mixingRounds, 
                        txRange):
    # init accounts
    accountsWhales = []
    for i in range(numWhales):
      accountsWhales.append(whalePreMine)
    accountsMed = []
    for i in range(numMedAccounts):
      accountsMed.append(medAccountsPreMine)
    accountsSmall = []
    for i in range(numSmallAccounts):
      accountsSmall.append(smallAccountsPreMine)
    accounts = accountsWhales + accountsMed + accountsSmall
    # mix account balances
    for i in range(mixingRounds):
        j = round(np.random.uniform(0, numAccounts - 1))
        k = round(np.random.uniform(0, numAccounts - 1))
        amount = np.random.uniform(0, txRange)
        if accounts[j] > amount:
            accounts[j] -= amount
            accounts[k] += amount
    # return accounts
    return accounts
accounts = createRandomAccounts(totalSupply, 
                                numAccounts, 
                                numWhales,
                                numMedAccounts,
                                numSmallAccounts,
                                whalePreMine,
                                medAccountsPreMine,
                                smallAccountsPreMine, 
                                mixingRounds, 
                                txRange)
print('\nAccounts:\n', accounts)

# Copy Original Accounts To Compare Later
def copyAccounts(accounts):
    copy = []
    for i in range(numAccounts):
        copy.append(round(accounts[i], 3))
    return copy
accountsBeforeVoting = copyAccounts(accounts)


# Quadratic Voting Costs with Collectively Distributed Payouts!
def vote(accounts, votingFee):
    # check if a player actually voted: -1 no, 0 did not vote, 1 yes
    allVotes = []
    votingAccounts = []
    for i in range(numAccounts):
        vote = np.random.randint(-1, 2)
        allVotes.append(vote)
        if vote != 0:
            votingAccounts.append(i)
    # check voter weight, process fee, and process vote
    totalVotingWeight = 0
    voterFeePool = 0
    voteOutcome = 0
    voterWeights = []
    for v in votingAccounts:
        totalVotingWeight += accounts[v]
    for v in votingAccounts:
        voterWeight = accounts[v] / totalVotingWeight
        voterWeights.append(voterWeight)
        # THIS IS WHERE THE QV FEE IS IMPLIMENTED
        # multiplying voterWeight by 10 to avoid the making the fee exponentially smaller rather than larger when you square voterWeight
        voterFee = votingFee * ((voterWeight*10)*(voterWeight*10))
        accounts[v] -= voterFee
        voterFeePool += voterFee
        voteOutcome += (allVotes[v] * voterWeight)
    # redistribute fees
    R = []
    n = 0
    for i in range(len(votingAccounts)):
        r = voterWeights[i] * voterFeePool
        R.append(r)
    for v in votingAccounts:
        accounts[v] += R[n]
        voterFeePool -= R[n]
        n += 1
    return voteOutcome

# Print Results
for i in range(votingRounds):
    vote(accounts, votingFee)
    if (i % printFrequency) == 0:
        print('\nAccounts After Round', i, '\n', accounts)


# Compare Original Accounts to End Game
# the whales should be losing money over time and the smaller accounts should be gaining money by participating
dif = []
for i in range(len(accounts)):
  dif.append(accounts[i] - accountsBeforeVoting[i])
print('\ndif:\n',dif)

# make sure we're not losing coins
print('\ntotal supply:',totalSupply)
oldAccountsSum = 0
for a in accountsBeforeVoting:
  oldAccountsSum += a
print('oldAccountsSum:',oldAccountsSum)
newAccountsSum = 0
for a in accounts:
  newAccountsSum += a
print('newAccountsSum:', newAccountsSum)

# If you want to test the mechanism with uniform accounts to verify that if an equilibrium is reached (what the cryptoeconomic version of that equilirbium actually is TBD), then the voting fee would not affect players in any way beyond constraining them to that equilibrium point. 
'''
# Test with Uniform Accounts (assuming everyone found the optimal size to maximize profits, whatever that might be)
def createUniformAccounts(totalSupply, numAccounts):
  accounts = []
  for i in range(numAccounts):
    accounts.append(totalSupply / numAccounts)
  return accounts
uniformAccounts = createUniformAccounts(totalSupply, numAccounts)
print('\nuniformAccounts:',uniformAccounts)

# Print Uniform Results
for i in range(votingRounds):
    vote(uniformAccounts, votingFee)
    if (i % printFrequency) == 0:
        print('\nUniform Accounts After Round', i+printFrequency, '\n', uniformAccounts)
'''
