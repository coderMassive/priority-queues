A = [] # list of keys
items = [] # list of items

def Set_Key(item, key):
  A[items.index(item)] = key

def Set_Value(key, item):
  items[A.index(key)] = item

def Order_Items(A, items):
  ordered_keys = sorted(A)
  ordered_items = []
  for j in range(len(A)):
    ordered_items.append("")
  for i in range(len(A)):
    if A[i] != ordered_keys[i]:
      ordered_items[ordered_keys[i]-1]=items[A[i]-1]
    else:
      ordered_items[i] = items[i]
  return [ordered_items, ordered_keys]
  
def Insert(key, value):
  A.append(key)
  items.append(value)

Insert(1, 1)
Insert(3, 3)
Insert(1, 2)
Insert(5, 4)
Insert(4, 4)
Set_Key(2, 2)
Set_Value(5, 5)

# order the items to match indeces
ordered = Order_Items(A, items)
items = ordered[0]
A = ordered[1]

print(items)
