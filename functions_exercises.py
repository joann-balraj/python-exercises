#!/usr/bin/env python
# coding: utf-8

#  ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


# our is_two defines a single parameter, x that is a string or number, and will return a boolean value
def is_two(x):
# Checks to see if the passed argument is equal to the number 2
    if x == 2:
# Returns boolean value if the above conditional is true
        return True
# If the passed argument is not equal to the number 2, checks to see if x is equal to the string '2'
    elif x == '2':
# Returns boolean value if the above conditional is true
        return True
# If x is not the number 2 or the string '2', returns boolean value "False"
    else: 
# Returns boolean value if both of the above conditionals were false
        return False


# #### Walkthrough:
# 1. When we pass `2` as an integer argument, the conditional first evaluates whether the argument is an integer. If the argument is an integer, like it is below, the code will return the boolean value true and the code will end there. 

# In[2]:


# Our integer test case:  
is_two(2)


# 2. When we pass `'2'` as a string value, the code first evaluates at the first conditional whether is it an integer. Because the string `'2'` is a string, the second conditional evaluates whether or not it is in fact the string `'2'`. The test case below would then go through the second conditional and return the boolean value "True" and the code would end there.

# In[3]:


# Our string test case:
is_two('2')


# 3. When we pass any argument that is neither the integer 2 nor the string '2', the argument would go through both of the first two conditionals and then get evaluated by the final conditional. This final conditional states that anything other than the integer `2` or the string `'2'` is false. The below test case would return the boolean value "False" and the code would end there.

# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[7]:


# Our is_vowel defines a single parameter, x that is a string, and will return a boolean value
def is_vowel(x):
# Checks to see if the passed argument is equal to the any one of these strings, which are the vowels
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
# Returns boolean value if the above conditional is true
        return True
# If the passed argument was not true, returns the boolean value "False"
    else:
        return False
# Our test case:
is_vowel('e')


# #### Walkthorugh:
# When we input the string argument `x` in the test case code, the first conditional evaluates whether `x` is equal to any one of the string values accepted (vowels). If the argument `x` is equal to a vowel, the code returns the boolean value "True". If `x` is not equal to a vowel, the code returns the boolean value "False".

# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[49]:


# Our is_consonant function defines a single parameter, x that is a string, and will return a boolean value
def is_consonant(x):
# Checks to see if the passed argument is equal to any of the string values in the code, returns "True"
    if x == 'B'or 'C' or 'D' or 'F' or 'G' or 'H' or 'J' or 'K' or 'L' or 'M' or 'N' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        return True
# If the passed argument is not equal to any of the accepted strings, the code returns "False"
    else:
        return False
# Our test case:
is_consonant('D')


# #### Walkthrough:
# When we input the string argument `x` in the test code, the first conditional evaluates whether `x` is equal to any of the string values (consanants). The `.upper()` function is also used in this conditional to capitalize any `x` input, in order to prevent the code from denying strings that are lowercase. The .upper() function just capitalizes any string input. If the string is equal to any consanant, the code returns the boolean value "True". If the passed string `x` does not equal a consant, the code returns the boolean value "False".

# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[51]:


# Our capitalize_consant function defines a single parameter, x that is a string, and will return the input capitalized when it contains a consanant
def capitalize_consonant(x):
# If the passed argument is equal to any of the string values in the code, returns the string input capitalized
    if x == 'B'or 'C' or 'D' or 'F' or 'G' or 'H' or 'J' or 'K' or 'L' or 'M' or 'N' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        print(x.capitalize())
# Our test case:
capitalize_consonant('codeup')
 


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[13]:


def calculate_tip(x, y):
    tip_percentage = x * y 
    return y - tip_percentage
# Our test case:
calculate_tip(.1, 20)
    
    


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[20]:


def apply_discount(x, y):
    discount = x * y
    return x - discount
# Our test case:
apply_discount(40, .2)


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[21]:


def handle_commas(x):
    return x.replace(',',"")
# Our test case:
handle_commas('1,000,000')


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[23]:


def get_letter_grade(x):
    if x >= 88 or x >= 100:
        print('A')
    elif x >= 80:
        print('B')
    elif x >= 67:
        print('C')
    elif x >= 60:
        print('D')
    else:
        print('F')
# Our test cases:
get_letter_grade(40)
get_letter_grade(60)
get_letter_grade(68)
get_letter_grade(80)
get_letter_grade(90)


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[39]:


def remove_vowels(x):
    x = x.replace('a', "")
    x = x.replace('e', "")
    x = x.replace('i', "")
    x = x.replace('o', "")
    return x.replace('u', "")
    
# Our test case:
remove_vowels('data science is sou cooooool')


# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# * anything that is not a valid python identifier should be removed
# * leading and trailing whitespace should be removed
# * everything should be lowercase
# * spaces should be replaced with underscores
# #### for example:
#   * Name will become name
#   * First Name will become first_name
#   * % Completed will become completed

# In[41]:


def normalize_name(x):

    x = x.lower().replace("*", "")
    x = x.replace("%", "")
    x = x.replace("0", "")
    x = x.replace("@", "")
    x = x.replace("$", "")
    x = x.replace("^", "")
    x = x.replace("&", "")
    x = x.replace("()", "")
    x = x.replace("0", "")
    x = x.replace(" ", "_")
    x = x.replace("1", "")
    x = x.replace("2", "")
    x = x.replace("3", "")
    x = x.replace("4", "")
    x = x.replace("5", "")
    x = x.replace("6", "")
    x = x.replace("7", "")
    x = x.replace("8", "")
    return x.replace("9", "")
 
# our test case:   
normalize_name("Jo ann*%019&()")


# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[6]:


def cumulative_sum(x):
# variable "new" has an empty list as it will be appended
   new = []
# variable "cumsum" set to 0 to later be assigned the result to the argument (x)
   cumsum = 0
   for x in x:
    # adds value (x) and the variable and assigns the result (cumsum) to that argument (x)
      cumsum += x
    # appends to "new", the list:
      new.append(cumsum)
    # returns the list that was appended with the cumulative sum of the list
   return new
# Our test case:
lists = [10, 20, 30, 40, 50]
print ("New list:",cumulative_sum(lists))


# In[ ]:




