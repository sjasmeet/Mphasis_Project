'''
1. Create a python method that takes arguments int X and int Y,
and updates DEPART and RETURN fields
in test_payload1.xml:

- DEPART gets set to X days in the future from the current date
(whatever the current date is at the moment of executing the code)
- RETURN gets set to Y days in the future from the current date

Please write the modified XML to a new file.

'''

from datetime import datetime, timedelta
import sys

def increase_days(d,num):
    return (datetime.strptime(d, '%Y%m%d') + timedelta(days=num)).strftime('%Y%m%d')

def update_depart_return_dates(x,y):
    xml_file = 'test_payload1.xml'
    xml_file_out = 'test_payload1_out.xml'
    try:
        f = open(xml_file)
        wf = open(xml_file_out,'w')
    except OSError:
        print("Could not read or write file: xml_file & xml_file_out\n")
        sys.exit()

    for line in f:
        if '<DEPART>' in line:
            old_date = line.split('>')[1].split('<')[0]
            new_date = increase_days(old_date,x)
            wf.write('{}{}{}\n'.format('      <DEPART>',new_date,'</DEPART>'))
            continue
        if '<RETURN>' in line:
            old_date = line.split('>')[1].split('<')[0]
            new_date = increase_days(old_date,y)
            wf.write('{}{}{}\n'.format('      <RETURN>',new_date,'</RETURN>'))
            continue
        wf.write(line)
    wf.close()

update_depart_return_dates(10,5)