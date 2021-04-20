import pandas as pd
import matplotlib.pyplot as plt

valores_vm_clone = [429,63.6,1056.6]
valores_net_conf = [5.4,5.4,33]
valores_vim_conf = [783.6,1.8,973.8]
valores_others = [83.4,0.6,147]

index = ['CORD','OSM','EALTEdge']

df = pd.DataFrame({'VM CLONE': valores_vm_clone, 'NET CONF': valores_net_conf,'VIM CONF': valores_vim_conf,
                    'OTHERS': valores_others}, index=index)

ax = df.plot.bar(rot=0, width=0.92, color={"VM CLONE": "black", "NET CONF": "dimgrey", 'VIM CONF': 'darkorange', 
                               'OTHERS': 'saddlebrown'})
plt.yscale('log')
ax.set_title("Deployments details")
ax.set_ylabel("Time (seg)")

plt.savefig("add_text_bar_matplotlib_02.png", bbox_inches='tight')
