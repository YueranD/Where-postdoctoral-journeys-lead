#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
%matplotlib inline

INDIR_DATA = 'data/'

def fig_1(df1, df2, props):
    # Who drops out of academia after a postdoc
    fig = plt.figure(figsize=(10,4))
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])
    # FIGURE 1A
    # delete negative infinity
    df1 = df1[df1['Imbalance_index_avg'] != 'negative infinity']
    df1['Imbalance_index_avg'] = df1['Imbalance_index_avg'].astype(float)
    ax1 = plt.subplot(gs[0])
    sns.scatterplot(
        data=df1, 
        x="Imbalance_index_avg", 
        y="Percentage", 
        size = 'count',
        sizes = (80,100),
        legend = False,
        ax=ax1)
    sns.lineplot(
        data=df1, 
        x="Imbalance_index_avg", 
        y="Percentage", 
        linewidth=props['linewidth'],
        ax=ax1)
    xnames = [-2.8, -0.8, -0.2, 0, 0.2, 0.4, 0.6, 0.8]
    plt.xticks(xnames)
    plt.xlabel('Relative change in publication rate\nbetween Ph.D. student and postdoc', fontsize=props['xylabel'])
    plt.ylabel('Percentage staying in academia', fontsize=props['xylabel'])
       
    # FIGURE 1B
    ax2 = plt.subplot(gs[1])
    plt.errorbar(
        x=df2['Hit papers'], 
        y=df2['Percentage'], 
        # yerr=df2['hindex_se'], 
        fmt=props['fmt'][0],
    )
    plt.xlabel('Hit papers', fontsize=props['xylabel'])
    plt.ylabel('Percentage staying in academia', fontsize=props['xylabel'])
    
    plt.show()
    
def fig_2(df1, df2, df3, df4, props):
    # Factors influencing the success of early career scientists.
    fig = plt.figure(figsize=(20,4))
    gs = gridspec.GridSpec(1, 4, width_ratios=[0.7, 1.3, 1, 1])  
    
    # FIGURE 2A
    ax1 = plt.subplot(gs[0])
    plt.errorbar(
        x = df1['Hit papers'],
        y = df1['hindex_mean'],
        yerr = df1['hindex_se'],
        ecolor = props['line_color'][0],
        markeredgecolor = props['line_color'][0],
        color = props['color'][0],
        fmt = props['fmt'][0],
        markersize = props['marker_size'],
    )
    plt.xlabel('Hit papers', fontsize=props['xylabel'])
    plt.ylabel('Success, η', fontsize=props['xylabel'])
    
    # FIGURE 2B
    ax2 = plt.subplot(gs[1])
    plt.errorbar(
        df2["research_field_diversity_mean"],
        df2["hindex_mean"],
        yerr=df2["hindex_se"],
        fmt = props['fmt'][0],
        ecolor=props['line_color'][1],
        markeredgecolor=props['line_color'][1],
        color=props['color'][1],
        elinewidth=props['linewidth'],
        markersize=props['marker_size'],
        # capsize=props['linewidth']
        )
    plt.xlabel('Topical difference, JSD', fontsize=props['xylabel'])
    plt.ylabel('Success, η', fontsize=props['xylabel'])
    
    # FIGURE 2C
    ax3 = plt.subplot(gs[2])
    color_dict = {category: color for category, color in zip(df3['Mobility'].unique(), props['color'])}
    ecolor_dict = {category: ecolor for category, ecolor in zip(df3['Mobility'].unique(), props['line_color'])}
    fmt_dict = {category: fmt for category, fmt in zip(df3['Mobility'].unique(), props['fmt'])}
    n_categories = df3['Mobility'].nunique()
    
    x_values = []
    x_labels = ['','','','Europe', 'US + Can.', 'Others']
    for i, mobility_category in enumerate(df3['Mobility'].unique()):
        mask = df3['Mobility'] == mobility_category
        x = np.arange(df3.loc[mask, 'phd_affiliation_district'].nunique()) + i * 0.2  # 保留位移        
        x_values.extend(x)

        plt.errorbar(
            x,
            df3.loc[mask, 'hindex_mean'],
            yerr = df3.loc[mask, 'hindex_se'],
            ecolor = ecolor_dict[mobility_category],
            markeredgecolor = ecolor_dict[mobility_category],
            color = color_dict[mobility_category],  
            fmt = fmt_dict[mobility_category],  
            elinewidth = props['linewidth'],
            markersize = props['marker_size'],
            # capsize=props['linewidth']
        )
    plt.xticks(x_values, x_labels)  
    plt.xlabel('Country of Ph.D.', fontsize=props['xylabel'])
    plt.ylabel('Success, η', fontsize=props['xylabel'])
    
    # FIGURE 2D
    ax4 = plt.subplot(gs[3])
    color_dict = {category: color for category, color in zip(df4['Mobility'].unique(), props['color'])}
    ecolor_dict = {category: ecolor for category, ecolor in zip(df4['Mobility'].unique(), props['line_color'])}
    fmt_dict = {category: fmt for category, fmt in zip(df4['Mobility'].unique(), props['fmt'])}
    n_categories = df4['Mobility'].nunique()

    x_values = []
    x_labels = ['','','','','','','Europe', 'US + Can.', 'Others']    
    for i, mobility_category in enumerate(df4['Mobility'].unique()):
        mask = df4['Mobility'] == mobility_category
        x = np.arange(df4.loc[mask, 'phd_affiliation_district'].nunique()) + i * 0.1
        x_values.extend(x)

        plt.errorbar(
            x,
            df4.loc[mask, 'hindex_mean'],
            yerr = df4.loc[mask, 'hindex_se'],
            ecolor = ecolor_dict[mobility_category],
            markeredgecolor = ecolor_dict[mobility_category],
            color = color_dict[mobility_category],  
            fmt = fmt_dict[mobility_category],  
            elinewidth = props['linewidth'],
            markersize = props['marker_size'],
            # capsize=props['linewidth']
        )
    plt.xticks(x_values, x_labels)  
    plt.xlabel('Country of Ph.D.', fontsize=props['xylabel'])
    plt.ylabel('Success, η', fontsize=props['xylabel'])
    
    
    
    
    

if __name__ == "__main__":
    
    # size, widths, coords
    plot_props = { 'xylabel' : 13,
        'figlabel' : 26,
        'ticklabel' : 15,
        'text_size' : 10,
        'marker_size' : 12,
        'linewidth' : 2,
        'tickwidth' : 1,
        'barwidth' : 0.8,
        'legend_prop' : { 'size':10 },
        'legend_hlen' : 1,
        'legend_np' : 1,
        'legend_colsp' : 1.1, 
        'color': ['#abb0d9', '#a7a9ac', '#d8d6a6', '#fbc4ae'],
        'line_color': ['#4b61ad', '#000000', '#a7a837', '#f37355'],
        'fmt': ['o', 's', 'v', '^']
    }
    
    df_dropout = pd.read_csv(INDIR_DATA+'fig1A_plot_dropout.csv')
    df_hit = pd.read_csv(INDIR_DATA+'fig1B_plot_hitpapers.csv')
    fig_1(df_dropout, df_hit, plot_props)
    
    df_hit_h = pd.read_csv(INDIR_DATA+'fig2A_plot_hitpapers.csv')
    df_topical_diff = pd.read_csv(INDIR_DATA+'fig2B_plot_topical_difference.csv')
    df_mobility_u = pd.read_csv(INDIR_DATA+'fig2C_plot_mobility_university.csv')
    df_mobility_t = pd.read_csv(INDIR_DATA+'fig2D_plot_mobility_top.csv')
    fig_2(df_hit_h, df_topical_diff, df_mobility_u, df_mobility_t, plot_props)
# %%
