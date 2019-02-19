def sum_to(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    print(sum) 
sum_to(10)



def largest(arrayofNums):
    largest = 0
    for num in arrayofNums:
        if (num > largest):
            largest = num
    print(largest)
        
largest([1,2,1231,12,9999])

def occurances(string, substr):
  mismatch = False
  count = 0
  if substr in string:
    for i in range( len(string) ):
      if string[i] == substr[0]:
        for j in range( len(substr) ):
          if substr[j] != string[i + j]:
            mismatch = True
            break;
        if not mismatch:
          count += 1
  print(string, substr, count)

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0


def product(*args):
  product = 1
  for arg in args:
    product *= arg
  print(product)
product(1,4,1,2,4,5)
