import re
import csv

with open('All_desktop.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

matches = re.findall(r'<tbody>(.*?)</tbody>', html_content, re.DOTALL)

out = [["CPU", "PRICE", "MULTI-PERF", "SINGLE-PERF"]]

if matches:
    last_tbody_content = matches[-1].strip()
    

    data = re.search(r'<tr role="row" class="odd">(.*?)</tr>', last_tbody_content, re.DOTALL);
    data = data.group(1).strip()

    
    cpu_list = re.findall(r'<td class="">\s*<a [^>]+>([^<]+)</a>\s*</td>', last_tbody_content, re.DOTALL);
    

    price = re.search(r'#price">(.*?)</a>', data, re.DOTALL);
    price = price.group(1).strip()

    price_list = re.findall(r'#price">(.*?)</a>', last_tbody_content, re.DOTALL);


    perf_list = re.findall(r'<td>(\d*,\d*)?(\d*)<\/td><td class=\"sorting_1\">(.*?)<\/td>', last_tbody_content, re.DOTALL);
    




    for i in range(cpu_list.__len__()):
        cpu = cpu_list[i]
        price = price_list[i]
        price = price.replace('$','')
        price = price.replace('*','')
        price = price.replace('NA','')

        multi = 0

        if(perf_list[i][0] == None):
            multi = perf_list[i][1]
            multi = multi.replace(',','')
        else:
            multi = perf_list[i][0]
            multi = multi.replace(',','')

        single = perf_list[i][2];
        single = single.replace(',','')


        out.append([cpu,price,multi,single])


    with open('cpu_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(out)

    print("Data written to cpu_data.csv")
else:
    print("No <tbody> found.")
