import matplotlib.pyplot as plt
import seaborn as sns

# clean - функция очистки и обработки данных
def clean(data):
    
    df = data.copy()
    df["furniture"] = df["furniture"].replace({"not furnished" :"0","furnished":"1"})
    df["animal"] = df["animal"].replace({"not acept":"0","acept":"1"})
    df["floor"] = df["floor"].replace({"-":"0"})
    df["hoa"] = df["hoa"].replace({"Sem info":"0","Incluso":"0"})
    df["property tax"] = df["property tax"].replace({"Incluso":"0"})
    
    for column in df.columns[8:]:
        df[column] = df[column].apply(lambda x: "".join(x.split("$")[-1].split(",")))
    
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype("int")
            
    return df

# hist - функция визуализации данных с помощью графика histplot
def hist(data, column, figsize=(15,5)):
    
    xlim = None
    if column == 'area':
        xlim = (0,900)
    elif column == 'rent amount':
        xlim = (0,25000)
    df = data[data[column] < xlim[1]]
    s = df[column]
    
    sns.set_style("whitegrid")
    sns.set_context('paper')
    plt.figure(figsize=figsize)
    
    sns.histplot(x=s,kde=True)
    plt.xlim(xlim)
    plt.ylabel("Count", fontsize=15)
    plt.xlabel(column.capitalize(), fontsize=15)
    plt.title(column.split()[0].capitalize() + " Distribution", fontsize=18);
    
# kde - функция визуализации данных с помощью графика kdeplot
def kde(data,figsize=(14,12)):
    l = ["Rent amount by location",
         "Total amount by location",
         "Fire insurance by location",
         "Property tax by location"]
    xlim = [[0, 20000],[0, 30000],[0, 300],[0, 6000]]
    cols = ['rent amount','total','fire insurance','property tax']
    
    sns.set(style='whitegrid')
    sns.set_context('paper')
   
    axs = []
    fig = plt.figure(figsize=figsize)
    axs.append(fig.add_subplot(2,2,1))
    axs.append(fig.add_subplot(2,2,2))
    axs.append(fig.add_subplot(2,2,3))
    axs.append(fig.add_subplot(2,2,4))
    
    for i in range(4):
        sns.kdeplot(x=data[data["city"] == 0][cols[i]],shade=True,ax=axs[i])
        sns.kdeplot(x=data[data["city"] == 1][cols[i]],shade=True,ax=axs[i])        
        axs[i].legend(["City","Out of City"],loc='upper right')
        axs[i].set_title(l[i], fontsize=18)
        axs[i].set_xlim(xlim[i])
        axs[i].set_xlabel(cols[i].capitalize(), fontsize=15)
        axs[i].set_ylabel("Destiny", fontsize=15)
        
        
    plt.tight_layout(pad=3.0);
    
# scatter - функция визуализации данных с помощью графика scatterplot
def scatter(data,figsize=(14,8)):
    sns.set_context('talk')
    plt.figure(figsize=(14,8))
    sns.scatterplot(data=data, x="total", y="area", hue="city",hue_order=[1,0])
    plt.xlabel("Total")
    plt.ylabel("Area")
    plt.xlim(0,33000)
    plt.ylim(0,1050);
    
# bar - функция визуализации данных с помощью графика barplot
def bar(data, figsize=(15,5)):
    sns.set_context('paper')
    axs = []
    fig = plt.figure(figsize=figsize)
    axs.append(fig.add_subplot(1,2,1))
    axs.append(fig.add_subplot(1,2,2))

    xticks = ["City","Out of City"]
    cols = ["total","area"]
    titles = ["Mean total","Mean area"]

    for i in range(2):
        sns.barplot(x="city",y=cols[i],data=data,order=[1,0],ax=axs[i])
        axs[i].set_xticklabels(xticks,fontsize=15)
        axs[i].set_xlabel("")
        axs[i].set_title(titles[i],fontsize=18)
        axs[i].set_ylabel(cols[i].capitalize(),fontsize=15)
    plt.tight_layout();
    
# bar2 - функция визуализации данных с помощью графика barplot
def bar2(data,figsize=(15,5)):
    plt.figure(figsize=figsize)
    sns.set_context('paper')
    sns.barplot(x="rooms",y='total',data=data)
    plt.title("Mean total by number of rooms",fontsize=18)
    plt.ylabel("Total",fontsize=15)
    plt.xlabel("Rooms",fontsize=15);

# pie - функция визуализации данных с помощью графика barplot
def pie(data,figsize=(9,9)):
    sns.set_context('talk')
    y = data["city"]
    plt.figure(figsize=figsize)
    plt.pie(y.value_counts().values,autopct="%.1f%%",
           explode=[0,0.1],labels=["City","Not City"])
    plt.title("Visualizing Class Imbalance")
    plt.show()