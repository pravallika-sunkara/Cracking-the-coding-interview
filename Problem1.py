
#Implement an algorithm to determine if a string has all unique characters . What if you cannot use additional data structures?



def Main():
  arr=[]
  s=raw_input("Enter your string:")
  for i in s:
    arr.append(i)
  uniq_char=[]
  for j in arr:
    if j in uniq_char:
      continue
    else:
      uniq_char.append(j)
  print "Unique characters in the string are:",uniq_char
  

if __name__=="__main__":
  Main()
