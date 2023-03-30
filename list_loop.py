
lst = list([2,3,6,6,5])
lst2 = list()

for lis in lst:
    if lis not in lst2:
        lst2.append(lis)
    else :
        continue
ordr = sorted(lst2, reverse=True)
print (ordr[1])