# CSV e HTML

import csv

html_output = ''
name = []

with open("Modulos/Prog12.csv", 'r') as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        name.append(line[0])

html_output += f'<p> there are currently {len(name)} </p>'
html_output += '\n<ul>'
for names in name:
    html_output += f'\n\t<li>{names}</li>' 
html_output += '\n</ul>' 
print(html_output)