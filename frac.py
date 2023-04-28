# https://youtu.be/sgD-GMBTpIc?t=920

res = 1
for i in range(51, 101):
    res = res - 1 / i
print(res)

denominator = 1
for i in range(51, 101):
    denominator = denominator * i
numerator = denominator
for i in range(51, 101):
    numerator = numerator - denominator / i
print(numerator / denominator)
