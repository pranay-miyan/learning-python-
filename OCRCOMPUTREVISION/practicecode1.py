egg = 0
pie = 0
tarts = 0
everything = 0
while everything != "y":
    egg = int(input("How many scotch eggs you want? (type end to stop) "))
    pie = int(input("How many pork pie you wants?(type end to stop) "))
    tarts = int((input("How many quiche tarts you want?(type end to stop) ")))
    everything = input("Is this everything y/n? ")

print(f"Your total will be {(egg*49)+(pie*85)+(tarts*145)}p .")
