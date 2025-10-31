import time
import matplotlib.pyplot as plt

# Initial setup
fair_value = 40
algo_bid = 20
algo_ask = 80
human_bid = 21
trade_executed = False

# Record data for visualization
algo_bids = [algo_bid]
algo_asks = [algo_ask]
human_bids = [human_bid]
steps = [0]

print("Initial Market: Algo Buyer @ 20, Seller @ 80")
print(f"Fair Value of Option = {fair_value}\n")

# Algo reacts to human order
step = 1
while not trade_executed:
    print(f"Step {step}: Human Buyer @ {human_bid}, Algo Buyer @ {algo_bid}, Algo Seller @ {algo_ask}")
    
    if human_bid < fair_value * 1.2:
        # Algo chases price upward till 20% above fair value
        algo_bid = human_bid + 1
        human_bid += 2  # human follows (gets greedy)
    else:
        # Trade happens: Algo sells to human
        print(f"\n💥 TRADE EXECUTED! Human buys from Algo at {human_bid}")
        print(f"Fair Value = {fair_value}, Human immediately loses ₹{human_bid - fair_value}")
        trade_executed = True
        
        # Algo resets
        algo_bid = 20
        algo_ask = 100
        print("\n🔁 Algo resets: Buyer @ 20, Seller @ 100\n")
    
    # Save for plotting
    algo_bids.append(algo_bid)
    algo_asks.append(algo_ask)
    human_bids.append(human_bid)
    steps.append(step)
    
    step += 1
    time.sleep(0.3)

# Plot behavior
plt.figure(figsize=(10,6))
plt.plot(steps, algo_bids, label='Algo Bid (Buyer)', marker='o')
plt.plot(steps, algo_asks, label='Algo Ask (Seller)', marker='x')
plt.plot(steps, human_bids, label='Human Buyer', marker='s')

plt.axhline(fair_value, color='gray', linestyle='--', label='Fair Value (₹40)')
plt.axhline(fair_value*1.2, color='red', linestyle='--', label='20% Above Fair Value (₹48)')

plt.title("Illiquid Option Market Simulation (Algo vs Human Trader)")
plt.xlabel("Step")
plt.ylabel("Option Price (₹)")
plt.legend()
plt.grid(True)
plt.show()
