import re

with open('dev.txt', 'r', encoding='utf-8') as f:
    content = f.read()

months_full = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
months_short = r'(Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
day = r'(0?[1-9]|[12][0-9]|30|31)'
month_numeric = r'(0[1-9]|1[0-2])'

pattern1 = r'\b' + day + r'\s+' + months_full + r'\b'
pattern2 = r'\b' + months_full + r'\s+' + day + r'\b'
pattern3 = r'\b' + months_short + r'\s+' + day + r'\b'
pattern4 = r'\b' + day + r'\.\s*' + months_full + r'\b'
pattern5 = r'(?<!\d|\.)(' + day + r'\.' + month_numeric + r')(?:\.\d{2,4})?(?!\d|\.)'
counter = 0

with open('results.txt', 'w', encoding='utf-8') as output:
    for match in re.finditer(pattern1, content, re.IGNORECASE):
        counter += 1
        print(match.group(0))
        output.write(str(counter) + ': ' + match.group(0) + '\n')

    for match in re.finditer(pattern2, content, re.IGNORECASE):
        counter += 1
        print(match.group(0))
        output.write(str(counter) + ': ' + match.group(0) + '\n')

    for match in re.finditer(pattern3, content, re.IGNORECASE):
        counter += 1
        print(match.group(0))
        output.write(str(counter) + ': ' + match.group(0) + '\n')

    for match in re.finditer(pattern4, content, re.IGNORECASE):
        counter += 1
        print(match.group(0))
        output.write(str(counter) + ': ' + match.group(0) + '\n')
        
    for match in re.finditer(pattern5, content, re.IGNORECASE):
        counter += 1
        print(match.group(1)) 
        output.write(str(counter) + ': ' + match.group(1) + '\n')
       
    print(f'Total dates found: {counter}')
    output.write(f'Total dates found: {counter}')