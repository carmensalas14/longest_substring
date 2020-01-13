"""
pedac 

p-
find the length of characters in a string that do not repeat 

e -
abbkewxrpbcc == 7

d -
input string
output integer

a -
loop over characters in string 
for every character store as property with a value of one in a dic
if thr charater repeats, add 1 to the value of the property for that charatcer

loop over dic and find which keys have a value of 1 the longest 
keeping track with a counter 
----

loop over string 
keep track of the length of characters until another character repeats 
store length of seperate substrings in dic 
return the key with the largest value 



"""

def longest_substring(string):
    dic = {
        substring:''
    }
    for letter in string:
        if letter in dic:
            dic[letter] = letter
        else:
            dic[substring] + letter
            
                
    print(dic)
    for key in dic:
        return max(len(key))
        
        

print(longest_substring(['abbkewxrpbcc']));

        
        
        
    