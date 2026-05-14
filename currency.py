print("Hi!")
pesos = float(input("How much do you have left in pesos?: "))
soles = float(input("How much do you have left in soles?: "))
reais = float(input("How much do you have left in reais?: "))
usd1 = (pesos * 0.00027)
usd2 = (soles * 0.29)
usd3 = (reais * 0.20)
totalUSD = usd1 + usd2 + usd3
print("You have", totalUSD, "dollars in total")


# You just got your first credit card!
# Each month, the bank adds interest to any unpaid balance. That means your debt can quietly grow...
# Let's see how much you’ll owe next month:
balance = 250.00
rate = 0.02
balance = balance + (balance * rate)
print(balance)