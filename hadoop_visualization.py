
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


t1 = pd.read_csv('./analyze_t1.csv')
t2 = pd.read_csv('./analyze_t2.csv')
t3 = pd.read_csv('./analyze_t3.csv')
t4 = pd.read_csv('./analyze_t4.csv')
t5 = pd.read_csv('./analyze_t5.csv')
t6 = pd.read_csv('./analyze_t6.csv')
t7 = pd.read_csv('./analyze_t7.csv')
t8 = pd.read_csv('./analyze_t8.csv')


# In[3]:


t1


# In[4]:


t1 = t1[t1["analyze_t1.provicne_id"].notnull()]#数据清洗，去掉NaN
t1


# In[5]:


t1[t1["analyze_t1.province_name"]=="黑龙江省"]["analyze_t1.orders"].values[0]


# ## 一、各省份销售额分析

# In[6]:


from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode


bias = 6000
example_data = [
    ("天津", [117.4219, 39.4189, int(t1[t1["analyze_t1.province_name"]=="天津"]["analyze_t1.orders"].values[0])]),
    ("山西", [112.3352, 37.9413, int(t1[t1["analyze_t1.province_name"]=="山西省"]["analyze_t1.orders"].values[0])]),
    ("陕西", [109.1162, 34.2004, int(t1[t1["analyze_t1.province_name"]=="陕西省"]["analyze_t1.orders"].values[0])]),
    ("甘肃", [103.5901, 36.3043, int(t1[t1["analyze_t1.province_name"]=="甘肃省"]["analyze_t1.orders"].values[0])]),
    ("青海", [101.4038, 36.8207, int(t1[t1["analyze_t1.province_name"]=="青海省"]["analyze_t1.orders"].values[0])]),
    ("四川", [103.9526, 30.7617, int(t1[t1["analyze_t1.province_name"]=="四川省"]["analyze_t1.orders"].values[0])]),
    ("重庆", [108.384366, 30.439702, int(t1[t1["analyze_t1.province_name"]=="重庆"]["analyze_t1.orders"].values[0])]),
    ("山东", [117.1582, 36.8701, int(t1[t1["analyze_t1.province_name"]=="山东省"]["analyze_t1.orders"].values[0])]),
    ("河南", [113.4668, 34.6234, int(t1[t1["analyze_t1.province_name"]=="河南省"]["analyze_t1.orders"].values[0])]),
    ("江苏", [118.8062, 31.9208, int(t1[t1["analyze_t1.province_name"]=="江苏省"]["analyze_t1.orders"].values[0])]),
    ("安徽", [117.29, 32.0581, int(t1[t1["analyze_t1.province_name"]=="安徽省"]["analyze_t1.orders"].values[0])]),
    ("湖北", [114.3896, 30.6628, int(t1[t1["analyze_t1.province_name"]=="湖北省"]["analyze_t1.orders"].values[0])]),
    ("浙江", [119.5313, 29.8773, int(t1[t1["analyze_t1.province_name"]=="浙江省"]["analyze_t1.orders"].values[0])]),
    ("福建", [119.4543, 25.9222, int(t1[t1["analyze_t1.province_name"]=="福建省"]["analyze_t1.orders"].values[0])]),
    ("江西", [116.0046, 28.6633, int(t1[t1["analyze_t1.province_name"]=="江西省"]["analyze_t1.orders"].values[0])]),
    ("湖南", [113.0823, 28.2568, int(t1[t1["analyze_t1.province_name"]=="湖南省"]["analyze_t1.orders"].values[0])]),
    ("贵州", [106.6992, 26.7682, int(t1[t1["analyze_t1.province_name"]=="贵州省"]["analyze_t1.orders"].values[0])]),
    ("广西", [108.479, 23.1152, int(t1[t1["analyze_t1.province_name"]=="广西"]["analyze_t1.orders"].values[0])]),
    ("海南", [110.3893, 19.8516, int(t1[t1["analyze_t1.province_name"]=="海南省"]["analyze_t1.orders"].values[0])]),
    ("上海", [121.4648, 31.2891, int(t1[t1["analyze_t1.province_name"]=="上海"]["analyze_t1.orders"].values[0])]),
    ("广东", [113.2730, 23.1176, int(t1[t1["analyze_t1.province_name"]=="广东省"]["analyze_t1.orders"].values[0])]),
    ("内蒙古", [111.8283, 40.8865, int(t1[t1["analyze_t1.province_name"]=="内蒙古"]["analyze_t1.orders"].values[0])]),
    ("云南", [102.8634, 24.8939, int(t1[t1["analyze_t1.province_name"]=="云南省"]["analyze_t1.orders"].values[0])]),
    ("北京",[116.397128,39.916527,int(t1[t1["analyze_t1.province_name"]=="北京"]["analyze_t1.orders"].values[0]-bias)]),
    ("黑龙江", [127.9688, 45.368, int(t1[t1["analyze_t1.province_name"]=="黑龙江省"]["analyze_t1.orders"].values[0])]),
    ("吉林", [125.8154, 44.2584, int(t1[t1["analyze_t1.province_name"]=="吉林省"]["analyze_t1.orders"].values[0])]),
    ("辽宁", [123.1238, 42.1216, int(t1[t1["analyze_t1.province_name"]=="辽宁省"]["analyze_t1.orders"].values[0])]),
    ("河北", [114.4995, 38.1006, int(t1[t1["analyze_t1.province_name"]=="河北省"]["analyze_t1.orders"].values[0])]),

]


# print(type(7405))
# print(type(t1[t1["analyze_t1.province_name"]=="北京"]["analyze_t1.orders"].values[0]))


c = (
    Map3D()
    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,23,11,0)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(
        series_name="bar3D",
        data_pair=example_data,
        type_=ChartType.BAR3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="各省份销售额"))
    .render("analyzed_pic1.html")
)
#c.render_notebook()


# In[7]:


t2


# ## 订单数量变化（弃用）

# In[8]:


# import pyecharts.options as opts
# from pyecharts.charts import Line
# from pyecharts.faker import Faker

# #print(type(t2["analyze_t2.orders"].values.tolist()))
# print(t2)
# #print(t2["analyze_t2.year"].values.tolist())
# #print(t2["analyze_t2.month"].values.tolist())
# ylist = t2["analyze_t2.year"].values.tolist()
# mlist = t2["analyze_t2.month"].values.tolist()
# dlist = []
# for i in range(len(ylist)):
#     d = str(ylist[i]) + "-" + str(mlist[i])
#     dlist.append(d)
    
# print(dlist)
# c1 = (
#     Line(init_opts=opts.InitOpts(width="800px", height="400px"))
#     .add_xaxis(dlist)
#     .add_yaxis("商家A", t2["analyze_t2.orders"].values.tolist(), is_smooth=True)
#     #.add_yaxis("商家B", t2["analyze_t2.sales"], is_smooth=True)
#     .set_series_opts(
#         areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="订单数量变化"),
#         xaxis_opts=opts.AxisOpts(
#             axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
#             is_scale=False,
#             boundary_gap=False,
#         ),
#     )
# )
# c1.render_notebook()
# # print(Faker.values())
# # print(Faker.values())


# ## 二、订单数量变化分析

# In[9]:


from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

#print(type(t2["analyze_t2.orders"].values.tolist()))
print(t2)
#print(t2["analyze_t2.year"].values.tolist())
#print(t2["analyze_t2.month"].values.tolist())
ylist = t2["analyze_t2.year"].values.tolist()
mlist = t2["analyze_t2.month"].values.tolist()
dlist = []
for i in range(len(ylist)):
    d = str(ylist[i]) + "-" + str(mlist[i])
    dlist.append(d)
    
#print(dlist)

c = (
    Bar()
    .add_xaxis(dlist)
    .add_yaxis("商家A", t2["analyze_t2.orders"].values.tolist(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="订单数量变化"))
    .render("analyzed_pic2.html")
)
#c.render_notebook()


# ## 三、销售总金额变化分析

# In[10]:


import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

# print(type(t2["analyze_t2.orders"].values.tolist()))
# print(t2)
# print(t2["analyze_t2.year"].values.tolist())
# print(t2["analyze_t2.month"].values.tolist())
ylist = t2["analyze_t2.year"].values.tolist()
mlist = t2["analyze_t2.month"].values.tolist()
dlist = []
for i in range(len(ylist)):
    d = str(ylist[i]) + "-" + str(mlist[i])
    dlist.append(d)
    
print(dlist)
c2 = (
    Line(init_opts=opts.InitOpts(width="800px", height="400px"))
    .add_xaxis(dlist)
    .add_yaxis("商家B", t2["analyze_t2.sales"].values.tolist(), is_smooth=True)
    .add_yaxis("商家B", Faker.values(), is_smooth=True)
    
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="订单数量变化"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
	.render("analyzed_pic3.html")
)
#c2.render_notebook()


# ## 四、各时段的订单数量与销售额分析

# In[11]:


from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

# print(t3["analyze_t3.orders"].values.tolist())
# print(t3["analyze_t3.sales"].values.tolist())

x_data = t3["analyze_t3.hour"].values.tolist()
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis(
        "订单数量",
        t3["analyze_t3.orders"].values.tolist(),
        yaxis_index=1,
        #color="#d14a61",
        color="#5768ff",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="订单数量",
            type_="value",
            min_=0,
            max_=55000,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#000000")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        )
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            #position='bottom',
            #is_show=True,
            is_scale=True,
            #offset=0,
            axisline_opts=opts.AxisLineOpts(
            is_show=False
            ),
            axistick_opts=opts.AxisTickOpts(
            is_show=False
            )
        ),
        
        yaxis_opts=opts.AxisOpts(
            name="销售额",
            min_=-150000000,
            max_=150000000,
            position="right",
            offset=0,
            axisline_opts=opts.AxisLineOpts(
                #linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                linestyle_opts=opts.LineStyleOpts(color="#000000")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}元"),
        ),
        title_opts=opts.TitleOpts(title="各时段的订单数量与销售额"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
    
)

line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "销售额",
        t3["analyze_t3.sales"].values.tolist(),
        yaxis_index=0,
        #color="#ff5798",
        #color="#BFEFFF",
        label_opts=opts.LabelOpts(is_show=False),
        
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            data=[
                opts.MarkAreaItem(name="午高峰", x=("12", "15")),
                opts.MarkAreaItem(name="晚高峰", x=("17", "20")),
            ]
        )
    )
)

# x_data = ["{}月".format(i) for i in range(1, 13)]
# line = (
#     Line()
#     .add_xaxis(x_data)
#     .add_yaxis(
#         "平均温度",
#         [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
# #         yaxis_index=2,
# #         color="#675bba",
# #         label_opts=opts.LabelOpts(is_show=False),
#     )
# )

#line.render_notebook()
#bar.render_notebook()
bar.overlap(line).render_notebook()

grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
#grid.render_notebook()
grid.render("analyzed_pic4.html")


# ## 五、客户公司订单金额排行

# In[12]:


from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

location = t4["analyze_t4.saledesc"][10:0:-1].values.tolist()
values = t4["analyze_t4.sales"][10:0:-1].values.tolist()


c = (
    PictorialBar(init_opts=opts.InitOpts(width="1600px", height="400px"))
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="客户公司订单金额排行"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("analyzed_pic5.html")
)
#c.render_notebook()


# ## 六、购买次数最高的用户词云

# In[13]:


import pyecharts.options as opts
from pyecharts.charts import WordCloud

#usr_count = t5["analyze_t5._c0"].values.tolist()

usr_count = t5["analyze_t5.count"].values.tolist()
usr_name = t5["analyze_t5.customername"].values.tolist()
data = [(usr_name[i],usr_count[i]) for i in range(len(usr_count))]
data

c=(
    WordCloud()
    .add(series_name="购买次数最高的用户词云", data_pair=data, word_size_range=[20, 100])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="购买次数最高的用户词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
	.render("analyzed_pic6.html")
)
#c.render_notebook()


# ## 七、商品的主要销售路线

# In[14]:


import pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd
from datetime import date
import datetime
from pyecharts.globals import WarningType

# 关闭warning
WarningType.ShowWarning = False

from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

allData = {
    "citys": [{
        "name": "沈阳",
        "value": [123.46987, 41.80515, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "北京",
        "value": [116.23128, 40.22077, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "张家口",
        "value": [115.282349, 40.974758, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "济南",
        "value": [116.75199, 36.55358, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "武汉",
        "value": [114.02919, 30.58203, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "长治",
        "value": [113.11649, 36.19581, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "嘉兴",
        "value": [120.78483, 30.74744, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "重庆",
        "value": [106.54041, 29.40268, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "泉州",
        "value": [118.613, 24.88946, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "吉林",
        "value": [126.57436, 43.88187, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "东莞",
        "value": [113.75179, 23.02067, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "大连",
        "value": [121.5255, 38.95223, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "深圳",
        "value": [113.88308, 22.55329, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }, {
        "name": "南昌",
        "value": [115.94422, 28.54538, 2],
        "symbolSize": 2,
        "itemStyle": {
            "normal": {
                "color": "#F58158"
            }
        }
    }],
    "moveLines": [
        {
        "fromName": "沈阳",
        "toName": "北京",
        "coords": [
            [123.46987, 41.80515],
            [116.23128, 40.22077]
        ]
        },{
        "fromName": "沈阳",
        "toName": "张家口",
        "coords": [
            [123.46987, 41.80515],
            [115.282349, 40.974758]
        ]
        },{
        "fromName": "沈阳",
        "toName": "济南",
        "coords": [
            [123.46987, 41.80515],
            [116.75199, 36.55358]
        ]
        },{
        "fromName": "沈阳",
        "toName": "武汉",
        "coords": [
            [123.46987, 41.80515],
            [114.02919, 30.58203]
        ]
        },{
        "fromName": "沈阳",
        "toName": "长治",
        "coords": [
            [123.46987, 41.80515],
            [113.11649, 36.19581]
        ]
        },{
        "fromName": "沈阳",
        "toName": "嘉兴",
        "coords": [
            [123.46987, 41.80515],
            [120.78483, 30.74744]
        ]
        },{
        "fromName": "沈阳",
        "toName": "重庆",
        "coords": [
            [123.46987, 41.80515],
            [106.54041, 29.40268]
        ]
        },{
        "fromName": "沈阳",
        "toName": "泉州",
        "coords": [
            [123.46987, 41.80515],
            [118.613, 24.88946]
        ]
        },{
        "fromName": "沈阳",
        "toName": "吉林",
        "coords": [
            [123.46987, 41.80515],
            [126.57436, 43.88187]
        ]
        },{
        "fromName": "沈阳",
        "toName": "东莞",
        "coords": [
            [123.46987, 41.80515],
            [113.75179, 23.02067]
        ]
        },{
        "fromName": "沈阳",
        "toName": "大连",
        "coords": [
            [123.46987, 41.80515],
            [121.5255, 38.95223]
        ]
        },{
        "fromName": "沈阳",
        "toName": "深圳",
        "coords": [
            [123.46987, 41.80515],
            [113.88308, 22.55329]
        ]
        },{
        "fromName": "沈阳",
        "toName": "南昌",
        "coords": [
            [123.46987, 41.80515],
            [115.94422, 28.54538]
        ]
        }
    ]
}

line_color_js = """
new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#58B3CC'
                }, {
                    offset: 1,
                    color: '#F58158'
                }], false)
"""
symbol_js = """function (data) {if(data[0]<-200) {return 10;} else {return 1;}}"""

geo = Geo(
    init_opts=opts.InitOpts(
        theme='dark',
        bg_color='#404a59',
        width='1000px',
        height='800px'))

city_data = []
for item in allData['citys']:
    geo.add_coordinate(item['name'], item['value'][0], item['value'][1])
    city_data.append([item['name'], item['value'][2]])

geo.add_schema(maptype="china", is_roam=False, zoom=1,
               itemstyle_opts=opts.ItemStyleOpts(
                   color="#323c48", border_color="#404a59"),
               emphasis_label_opts=opts.LabelOpts(is_show=False),
               emphasis_itemstyle_opts=opts.ItemStyleOpts(color="#2a333d"))
geo.add(
    "",
    city_data,
    type_='effectScatter',
    symbol_size=JsCode(symbol_js),
    itemstyle_opts=opts.ItemStyleOpts(color='#46bee9'),
    #effect_opts=opts.EffectOpts(is_show=True, symbol='pin', brush_type='stroke')
)
geo.add(
    "",
    [(item['fromName'], item['toName']) for item in allData['moveLines']],
    is_large=True,
    type_='lines',
    symbol='pin',
    effect_opts=opts.EffectOpts(
        symbol='pin', symbol_size=3, trail_length=0),
    linestyle_opts=opts.LineStyleOpts(
        width=1, curve=0.1, opacity=0.3, color=JsCode(line_color_js)),
)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(legend_opts=opts.LegendOpts(is_show=True),
                    title_opts=opts.TitleOpts(title="商品的主要销售路线", pos_left='center',
                                              title_textstyle_opts=opts.TextStyleOpts(color='#fff')))


#geo.render_notebook()
geo.render("analyzed_pic7.html")


# ## 八、按地域分析订单数量比例

# In[15]:


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

region_name = t7["analyze_t7.region_name"].values.tolist()
region_amount = t7["analyze_t7.orders_amount"].values.tolist()

x = region_name#存储区域名
y = region_amount#存储订单数量

c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))#初始化饼状图
    .add("", [list(z) for z in zip(x, y)])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))#显示标签
)

#c.render_notebook()
c.render("analyzed_pic8.html")


# ## 九、按地域分析销售额比例

# In[16]:


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

region_name = t8["analyze_t8.region_name"].values.tolist()
region_amount = t8["analyze_t8.total_payment"].values.tolist()

x = region_name#存储区域名
y = region_amount#存储订单数量

c = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))#初始化饼状图
    .add("", [list(z) for z in zip(x, y)])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))#显示标签
)

#c.render_notebook()
c.render("analyzed_pic9.html")

