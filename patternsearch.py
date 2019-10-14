import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Using the findall function, get all of the instances of non alphanumeric characters in the string assigned to 'lorem_ipsum'
#Output to the console, the number of non-alphanumeric characters.  Hint:  use the len function

pattern = "[^a-zA-z]"
results = re.findall(pattern, lorem_ipsum)
print(len(results))

pattern = "sit[:-]amet"
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

pattern = "sit[:-]amet"
replace = re.sub(pattern,'sit amet', lorem_ipsum)
replace_results = re.findall('sit amet', replace)
print(len(replace_results))