# violin plot function to help iterative plotting

import seaborn as sns
import matplotlib.pyplot as plt

def violin_plot(df, title, y, scale ='area', bw = 'scott', fig_width = 10, fig_height = 6, inner = 'box', split = True, hue = None):
    
    sns.set(rc={"figure.figsize":(fig_width, fig_height)}); #width=8, height=4
    ax = sns.violinplot(data=df, x="all", y=y, hue=hue, split=split, scale=scale, bw = bw, inner = inner);
    ax.set(xlabel=y, ylabel = 'Value');
    ax.set_title(title + '_' + scale + '_' + bw);

    return ax