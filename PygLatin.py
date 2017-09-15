# Let's warm up by printing a welcome message for our translator users.
# Next, we need to ask the user for input.

# print 'Welcome to the Pig Latin Translator!'

# original = raw_input("Enter a word: ")

# Next we need to ensure that the user actually typed something.

# if len(original) > 0:
  # print original
# else:
  # print "empty"
  
 # 1. Use and to add a second condition to your if statement. In addition to your existing check that the string contains 
 # characters, you should also use .isalpha() to make sure that it only contains letters. 
 # if len(original) > 0 and original.isalpha(): print original

# to translate to pig latin, move the first letter of the word to the end and then append the suffix 'ay'. 
# Example: python -> ythonpay
# Create a variable named pyg and set it equal to the suffix 'ay'.

# Let's simplify things by making the letters in our word lowercase.
# We also need to grab the first letter of the word.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  	word = original.lower()
  	first = original[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
else:
    print 'empty'
print new_word
    
# Now that we have the first letter stored, 
# we need to add both the letter and the string stored in pyg to the end of the original string. CONCATENATE
# btwn first variable and print command:    new_word = word + first + pyg
# However, now we have the first letter showing up both at the beginning and near the end.. We are going to slice the string
# : new_word = new_word[1:len(new_word)]


