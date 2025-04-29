from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
f=open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines=f.readlines()
data_lines.pop(0)
data_dict={}
timeline=Timeline({"theme":ThemeType.LIGHT})
for line in data_lines:
    year=int(line.split(",")[0])
    country=line.split(",")[1]
    gdp=float(line.split(",")[2])
    try:
        data_dict[year].append([country,gdp])
    except:
        data_dict[year]=[]
        data_dict[year].append([country,gdp])
sorted_year=sorted(data_dict.keys())
for year in sorted_year:
    data_dict[year]=sorted(data_dict[year],key=lambda x:x[1],reverse=True)
    country_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country in country_data:
        x_data.append(country[0])
        y_data.append(country[1]/100000000)
    bar=Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("各国GDP排名(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar,f"{year}年")
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年各国GDP排名"),
    )
timeline.add_schema(
        play_interval=1000,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=False
    )
timeline.render("timeline.html")