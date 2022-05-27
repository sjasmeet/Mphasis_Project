'''3. Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV).
'''

import datetime

def analyze_jmeter_logs(*files):
    print('{},{},{},{},{}'.format('label', 'response_code', 'response_message', 'failure_message', 'pst_time'))

    for file in files:
        for line in open(file):
            if line.startswith('timeStamp') or len(line) <= 1:
                continue
            line = line.rstrip()
            fields = line.split(',')
            label,response_code,response_message,failure_message,timestamp = fields[2],fields[3],fields[4],fields[8],fields[0]
            if response_code == '200':
                continue
            pst_time = datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime("%Y-%m-%d %H:%M:%S")

            print('{},{},{},{},{}'.format(label,response_code,response_message,failure_message,pst_time))

analyze_jmeter_logs('Jmeter_log1.jtl','Jmeter_log2.jtl')