# takes in a price without GST, calculates GST, and adds it to the price
def calc_gst(net_price):
    return net_price * 1.15


# Main routine
net_price_ = float(input("Enter the net price $"))
print(f"${calc_gst(net_price_):.2f}")


