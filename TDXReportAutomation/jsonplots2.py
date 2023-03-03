import json
import matplotlib.pyplot as plt
import mpld3

fig, axs = plt.subplots(4, 2, figsize=(10, 10))

with open('response1.json') as f:
    data = json.load(f)

labels = [row['ResponsibleGroupName'] for row in data['DataRows']]
values = [row['CountTicketID'] for row in data['DataRows']]

axs[0, 0].barh(labels, values, color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[0, 0].set_title(data['Name'], fontsize=10, fontweight='bold')


with open('response2.json') as f:
    data2 = json.load(f)

labels = [row['ResponsibleFullName'] for row in data2['DataRows']]
values = [row['CountTicketID'] for row in data2['DataRows']]

axs[0, 1].bar(labels, height=values, color=['darkblue', 'palegreen', 'limegreen', 'aquamarine'])
axs[0, 1].set_title(data2['Name'], fontsize=10, fontweight='bold')


with open('response3.json') as f:
    data3 = json.load(f)

labels = [row['TypeName'] for row in data3['DataRows']]
values = [row['CountTicketID'] for row in data3['DataRows']]

axs[1, 0].pie(values, labels=labels, autopct='%1.1f%%', colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[1, 0].set_title(data3['Name'], fontsize=10, fontweight='bold')


with open('response4.json') as f:
    data4 = json.load(f)

labels = [row['Responsibility'] for row in data4['DataRows']]
values = [row['CountTicketID'         ] for row in data4['DataRows']]

axs[1, 1].pie(values, labels=labels, autopct='%1.1f%%', colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[1, 1].set_title(data4['Name'], fontsize=10, fontweight='bold')

with open('response5.json') as f:
    data5 = json.load(f)

labels = [row['TypeName'] for row in data5['DataRows']]
values = [row['CountTicketID'] for row in data5['DataRows']]

axs[2, 0].barh(labels, values, color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[2, 0].set_title(data['Name'], fontsize=10, fontweight='bold')

with open('response6.json') as f:
    data6 = json.load(f)

labels = [row['Responsibility'] for row in data6['DataRows']]
values = [row['CountTicketID'] for row in data6['DataRows']]

axs[2, 1].pie(values, labels=labels, autopct='%1.1f%%', colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[2, 1].set_title(data6['Name'], fontsize=10, fontweight='bold')

with open('response7.json') as f:
    data7 = json.load(f)

labels = [row['TypeName'] for row in data7['DataRows']]
values = [row['CountTicketID'] for row in data7['DataRows']]

axs[3, 0].barh(labels, values, color=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[3, 0].set_title(data['Name'], fontsize=10, fontweight='bold')


with open('response8.json') as f:
    data8 = json.load(f)

labels = [row['Responsibility'] for row in data8['DataRows']]
values = [row['CountTicketID'] for row in data8['DataRows']]

axs[3, 1].pie(values, labels=labels, autopct='%1.1f%%',colors=['Cyan', 'darkblue', 'lightseagreen', 'springgreen'])
axs[3, 1].set_title(data8['Name'])

plt.subplots_adjust(wspace=0.1, hspace=0.1)

plt.show()
plt.tight_layout()
html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()