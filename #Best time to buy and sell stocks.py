# Best Time to Buy and Sell Stock
# Time Complexity:  O(n) — one pass through the prices array
# Space Complexity: O(1) — only two variables, no extra data structures

class solution:
    def maxProfit(self, prices):
        # Start min at infinity so the first price always becomes the minimum
        minimum_price = float('inf')

        # Start profit at 0 — return 0 if no profit is possible
        maximum_profit = 0

        for price in prices:
            # If today's price is cheaper than anything we've seen, update our best buy day
            if price < minimum_price:
                minimum_price = price

            # Calculate profit if we sell TODAY (today's price - cheapest buy so far)
            profit = price - minimum_price

            # Keep track of the best profit we've seen across all days
            maximum_profit = max(profit, maximum_profit)

        return maximum_profit

s = solution()
s.maxProfit([7, 1, 5, 3, 6, 4])