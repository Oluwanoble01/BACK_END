#create the dictionary
dictionary = { 'D' : '(D)' , 'A' : 'mnm' }

#open the text file in read only mode
text_file = open("Ecoli.txt", "r")

#To open a modified text file
modified_text_file = open("modified_text_file.txt", "w")

for x in text_file:
        if x[0] != ">":   #To skip every line that starts with '>' in the text file
         for key in dictionary:
                x = x.replace(key, dictionary[key])  #To perform the replacement using the values of the created dictionary
         modified_text_file.write(x)
        else:
            modified_text_file.write(x)

modified_text_file.close()
text_file.close()

