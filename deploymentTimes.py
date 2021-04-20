import matplotlib.pyplot as plt

fig, ax = plt.subplots()

bar_x = [1,2,3]
bar_height = [1277.4,71.4,2188.8]
bar_tick_label = ['CORD','OSM','EALTEdge']
bar_label = [1277.4,71.4,2188.8]

bar_plot = plt.bar(bar_x,bar_height,tick_label=bar_tick_label, color="black")

def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                bar_label[idx],
                ha='center', va='bottom', rotation=0)

autolabel(bar_plot)

#plt.yscale('log')

# A label para o eixo Y
plt.ylabel('Time (seg)')

plt.title('Deployment times in VIM-ON-DEMAND')

plt.savefig("add_text_bar_matplotlib_01.png", bbox_inches='tight')
plt.show()
