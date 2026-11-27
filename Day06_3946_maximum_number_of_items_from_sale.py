
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)
        bonus = [0] * n

        # Calculate free items
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        # Dynamic Programming
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            free = bonus[i]

            old = dp[:]
            new = dp[:]

            for b in range(price, budget + 1):

                # First purchase
                new[b] = max(
                    new[b],
                    old[b - price] + 1 + free
                )

                # Additional purchases
                new[b] = max(
                    new[b],
                    new[b - price] + 1
                )

            dp = new

        return dp[budget]
