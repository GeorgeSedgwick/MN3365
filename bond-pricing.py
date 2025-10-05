

face_value = float(input("What is the face value of the bond?\n> "))
coupon_rate = float(input("What is the coupon rate of the bond?(%)\n> ")) / 100
maturity = int(input("What is length-to-maturity of the bond?(years)\n> "))
r = float(input("What is the required rate of return?(%)\n> ")) /  100

coupon = face_value * coupon_rate

pv = 0
for i in range (1, maturity + 1):
    if i == maturity:
        pv += (coupon + face_value) / (1 + r)**i
    else:
        pv += coupon / (1 + r)**i

print(f"Price of bond: {round(pv, 2)}")
