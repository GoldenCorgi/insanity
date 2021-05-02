import os


real= 0
for root in os.listdir('../'):
    if root[:4] in ["2019","2020","2021"]:

        print(f'''<li><a href="#{root.replace(" ","-")}">{root}</a></li>''')


for root in os.listdir('../'):
    if root[:4] in ["2019","2020","2021"]:

        print(f'''## {root}\n**Notes:** \n''')
