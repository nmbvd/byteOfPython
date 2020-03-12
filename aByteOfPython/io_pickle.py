import pickle
filename='shoplist.data'
shoplist=['apple', 'mango', 'carrot']

with open (filename,'wb') as f:
    pickle.dump(shoplist,f)
del shoplist
try:
    print(shoplist)
except Exception:
    print("shop list dos not exist!")

with open(filename,'rb') as f:
    sl=pickle.load(f)
    print(sl)
