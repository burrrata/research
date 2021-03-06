## QVACG: quadratic voting anti centralization gadget
- https://ethresear.ch/t/quadratic-costs-and-collective-payouts-as-anti-centralization-gadget/2429
- imposing quadratic costs may put pressure on the players of a game to move towards a maximally effecient equilibrium
- the rules that impose that quadratic cost define the eqiulibrium points players move to, and thus the degree of centralization/decentralization
- quadratic costs/benefits can be maximally effective in iterative games that are rolled out indefinitely (incentivizing participants to move to the equilibrium immediately as there no benefit in resisting)

<br>

## CTMPD: charity through marginal price discrimination
- original idea: https://vitalik.ca/jekyll/general/2017/03/11/a_note_on_charity.html
- it seems like in a setting like Charity Through Marginal Price Discrimination the system works in isolation, but would be maximally effective in a setting with multiple participants all putting pressure on each other to opt into a shared mechanism. 
- moving towards a mechanism that can test and compare arbitrary populations
- and then evolve populations to over iterated games (simulating people finding value in a mechanism and adopting it)
Also considering how this could be implimented in the real world, and if the same mechanism might inspire cartell/monopoly type behavior if used for marketing/promotion/upsell mechanisms rather than community building. Attacks and defenses TBD.

<br>

## PoS HashCash Signalling
- continuing ideas from this thread: https://ethresear.ch/t/conditional-proof-of-stake-hashcash/1301/18
- also inspired by this post: http://gabethebassplayer.tumblr.com/post/180605851475/show-rating
- relevant to marginal price discrimination because it's all about pricing that incentivizes signal > noise and reduces spam/cheating, esp in social contexts and larger games of life.

<br>

## Future Work

To really roll these out, we need to model both honest and malicious populations to determine up to what threshold attacks will fail or become profitable. This requires:
- functions that can generate arbitrary populations with various metrics/parameters
- functions that can iterate over those populations and test for thresholds of success/failure
- functions that can iterate over populations over the course of repeat interactions over time and test for thresholds of success/failure

<br>
