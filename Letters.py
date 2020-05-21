
user_input = input("please write a sentence :  ")

letter_freq = {} 
  
for i in user_input: 
    if i in letter_freq: 
        letter_freq[i] += 1
    else: 
        letter_freq[i] = 1
print (letter_freq)
