import re 

newOutput = open('CleanedOutputs.txt', 'w')

with open ('output.txt', 'r') as newFile:
	data = newFile.read()
	clean_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",data).split())
newOutput.write(clean_text+'\n')
newFile.close()
newOutput.close()
print ("Cleaned.")