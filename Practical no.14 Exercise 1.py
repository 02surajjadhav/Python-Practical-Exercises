# VI Exercise 1
# Survey Analytics Tool

products = ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
            "Laptop", "Tablet", "Mobile", "Laptop"]

votes = {
    "Laptop": 0,
    "Mobile": 0,
    "Tablet": 0
}

# Count votes dynamically
for product in products:
    if product in votes:
        votes[product] += 1
    else:
        votes[product] = 1

# Display vote counts
print("----- SURVEY RESULTS -----")

for product in votes:
    print(product, ":", votes[product], "votes")

# Find winner
winner = max(votes, key=votes.get)

print("\nWinner:", winner)
print("Votes:", votes[winner])
