import re

x="Process finished with exit code 0"
y=re.findall('Process',x)
print(y)