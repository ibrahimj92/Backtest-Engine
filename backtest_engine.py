import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
days = 200
returns = np.random.normal(0.0005, 0.009, size=days)
equity = 100000 * (1 + pd.Series(returns)).cumprod()

print("[INFO] Final portfolio value:", round(equity.iloc[-1], 2))

plt.plot(equity.index, equity.values)
plt.title("Strategy Backtest — Equity Curve")
plt.xlabel("Day"); plt.ylabel("Portfolio Value (£)")
plt.tight_layout()
plt.savefig("backtest_equity_curve.png", dpi=200, bbox_inches="tight")
print("[INFO] Saved chart -> backtest_equity_curve.png")