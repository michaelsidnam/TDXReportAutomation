import json
import matplotlib.pyplot as plt
import mpld3



plt.figure(figsize=(10, 8)) # Adjust figure size

with open('response1.json') as f:
    data = json.load(f)

labels = [row['ResponsibleGroupName'] for row in data['DataRows']]
values = [row['CountTicketID'] for row in data['DataRows']]

ax1 = plt.subplot(2, 2, 1)
ax1.pie(values, labels=labels, autopct='%1.1f%%')
ax1.tick_params(labelsize=12) # Adjust font size
ax1.set_title(data['Name'], fontsize=14) # Adjust font size and title

with open('response2.json') as f:
    data2 = json.load(f)

labels = [row['ResponsibleFullName'] for row in data2['DataRows']]
values = [row['CountTicketID'] for row in data2['DataRows']]

ax2 = plt.subplot(2, 2, 2)
ax2.pie(values, labels=labels, autopct='%1.1f%%')
ax2.tick_params(labelsize=12) # Adjust font size
ax2.set_title(data2['Name'], fontsize=14) # Adjust font size and title

with open('response3.json') as f:
    data3 = json.load(f)

labels = [row['TypeName'] for row in data3['DataRows']]
values = [row['CountTicketID'] for row in data3['DataRows']]

ax3 = plt.subplot(2, 2, 3)
ax3.pie(values, labels=labels, autopct='%1.1f%%')
ax3.tick_params(labelsize=12) # Adjust font size
ax3.set_title(data3['Name'], fontsize=14) # Adjust font size and title

with open('response4.json') as f:
    data4 = json.load(f)

labels = [row['Responsibility'] for row in data4['DataRows']]
values = [row['CountTicketID'] for row in data4['DataRows']]

ax4 = plt.subplot(2, 2, 4)
ax4.pie(values, labels=labels, autopct='%1.1f%%')
ax4.tick_params(labelsize=10) #

fig, axs = plt.subplots(2, 2)

plt.tight_layout()
html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()