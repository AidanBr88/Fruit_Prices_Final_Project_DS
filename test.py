import pandas as pd

# Load the CSV file
df = pd.read_csv("Fruit-Prices-2022.csv")

# Clean column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# Optional: Print column names to verify
# print(df.columns.tolist())

# === Query 1: Fresh fruit with highest cup equivalent price ===
print("=== Query 1: Fresh fruit with highest cup equivalent price ===")
q1 = df[df['Form'] == 'Fresh'].sort_values('CupEquivalentPrice', ascending=False).head(1)
print(q1[['Fruit', 'Form', 'CupEquivalentPrice']])
print()

# === Query 2: Top 5 cheapest canned fruits by cup equivalent price ===
print("=== Query 2: Top 5 cheapest canned fruits by cup equivalent price ===")
q2 = df[df['Form'] == 'Canned'].sort_values('CupEquivalentPrice').head(5)
print(q2[['Fruit', 'Form', 'CupEquivalentPrice']])
print()

# === Query 3: Cheapest form of strawberries per cup ===
print("=== Query 3: Cheapest form of strawberries per cup ===")
q3 = df[df['Fruit'].str.contains('Strawberries')].sort_values('CupEquivalentPrice').head(1)
print(q3[['Fruit', 'Form', 'CupEquivalentPrice']])
print()

# === Query 4: Average cup equivalent price of dried fruits ===
print("=== Query 4: Average cup equivalent price of dried fruits ===")
q4 = df[df['Form'] == 'Dried']['CupEquivalentPrice'].mean()
print(f"Average price per cup for dried fruits: ${q4:.2f}")
print()

# === Query 5: Fruits with yield < 0.7 and cup price > $1.50 ===
print("=== Query 5: Fruits with yield < 0.7 and cup price > $1.50 ===")
q5 = df[(df['Yield'] < 0.7) & (df['CupEquivalentPrice'] > 1.50)]
print(q5[['Fruit', 'Form', 'Yield', 'CupEquivalentPrice']])
print()

# === Query 6: Top 3 most expensive fruits per cup ===
print("=== Query 6: Top 3 most expensive fruits per cup ===")
q6 = df.sort_values('CupEquivalentPrice', ascending=False).head(3)
print(q6[['Fruit', 'Form', 'CupEquivalentPrice']])

