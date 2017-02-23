def freq_analysis(message):
    freq_list = [0] * 26
    for char in message:
        for i in range(0,26):
            if char == chr(i + 97):
                freq_list[i] += (1. / len(message))
    ##
    # Your code here
    ##
    return freq_list

anal = freq_analysis('this has been a test')
letters = ['a'] * 26
for i in range(0,26):
    letters[i] = chr(i + 97)

for i in range(0,26):
    print str(anal[i]) + letters[i]
