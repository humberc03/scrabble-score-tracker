from .clear import clear

#Sub
def subValidateStart(extender):

  #receives a new input from the user
  clear()
  print("You must input " + extender)
  x = input("\n >> ")

  #returns the new input
  return x
#Sub

#One Number
def oneNumValidate(x,extender,numOne):

  #ensures the input is a number within range
  if any(c.isalpha() for c in x) == True:
    x = oneNumSubValidate(x,extender,numOne)
  if int(x) < numOne:
      x = oneNumSubValidate(x,extender,numOne)
 
  #returns the validated input
  return x

def oneNumSubValidate(x,extender,numOne):
  
  #gets new input
  x = subValidateStart(extender)
  return oneNumValidate(x,extender,numOne)
#One Number

#Two Number
def twoNumValidate(x,extender,numOne,numTwo):
  
  #ensures the input is a number within range
  if any(c.isalpha() for c in x) == True:
    x = twoNumSubValidate(x,extender,numOne,numTwo)
  if int(x) < numOne or int(x) > numTwo:
      x = twoNumSubValidate(x,extender,numOne,numTwo)
  
  #returns the validated input
  return x

def twoNumSubValidate(x,extender,numOne,numTwo):
  
  #gets new input
  x = subValidateStart(extender)
  return twoNumValidate(x,extender,numOne,numTwo)
#Two Number
