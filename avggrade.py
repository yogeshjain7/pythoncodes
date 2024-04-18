d={None}
try:
    avg=sum(d.values())
    avg/=3
    print("average of these marks are:", avg)
except:
    print("dictionary is empty")
