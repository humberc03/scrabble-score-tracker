def binarySearch(array, target):

  #sets up the search
  first = 0
  last = len(array)-1
  found = False

  #defines the midpoint of the array
  while first <= last and not found:
    midpoint = (first + last)//2

    #detects if the current midpoint is equal to the target
    if array[midpoint].idnum == target:
      found = True
    
    #if not, and target is LESS than midpoint, switches to first half of list, if it is GREATER than midpoint, switches to second half
    else:
      if target < array[midpoint].idnum:
        last = midpoint - 1
      else:
        first = midpoint + 1
	
  #returns location of target
  return midpoint
