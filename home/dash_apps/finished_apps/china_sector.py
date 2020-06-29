from django.shortcuts import render
from django.http import HttpResponse
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#import data
from home.dash_apps.dataset import dataset_var as ds

def ChinaMap_confirmed():

    ch_latest = ds.ch_latest

    ch_latest = ch_latest[['Date','Province/State', 'Lat', 'Long', 'Confirmed', 'Deaths', 
                            'Recovered', 'Active']]
    ch_latest_grouped = ch_latest.groupby(['Province/State', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    ch_latest_grouped['desc'] = ch_latest_grouped.agg('{0[Province/State]} : {0[Confirmed]}'.format, axis=1)
    ch_latest_grouped['size'] = ch_latest_grouped['Confirmed'].pow(0.7)

    cases = []
    cases.append(go.Scattergeo(
        lon = ch_latest_grouped['Long'],
        lat = ch_latest_grouped['Lat'],
        hovertext=ch_latest_grouped['desc'],
        marker = dict(
                size = ch_latest_grouped['size'],
                color='blue',
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
    ) )

    layout = go.Layout(
        title="Peta China dengan Kasus Terkonfirmasi",
        geo = dict(
            resolution = 50,
            bgcolor= 'rgba(0,0,0,0)',
            scope = 'asia',
            showframe = False,
            showcoastlines = True,
            showland = True,
            landcolor = "#989898",
            countrycolor = "rgb(255, 255, 255)" ,
            coastlinecolor = "rgb(255, 255, 255)",
            projection = dict(
                type = 'mercator',
                scale= 2
            ),
            center = dict(
                lon=98.044117,
                lat=36.058394
            )
        ),
        font = {"size": 9, "color":"White"},
        titlefont = {"size": 20, "color":"White"},
        paper_bgcolor='#303030 ',
        plot_bgcolor='#303030 ',
        width=620,
        height=500,
    )

    fig = go.Figure(layout=layout, data=cases)

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def chinaMap_deaths():

    ch_latest = ds.ch_latest

    ch_latest_grouped = ch_latest.groupby(['Province/State', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    ch_latest_grouped['desc'] = ch_latest_grouped.agg('{0[Province/State]} : {0[Deaths]}'.format, axis=1)
    ch_latest_grouped['size'] = ch_latest_grouped['Deaths'].pow(0.9)

    cases = []
    cases.append(go.Scattergeo(
        lon = ch_latest_grouped['Long'],
        lat = ch_latest_grouped['Lat'],
        hovertext=ch_latest_grouped['desc'],
        marker = dict(
                size = ch_latest_grouped['size'],
                color='red',
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
    ) )

    layout = go.Layout(
        title="Peta China dengan Kasus Meninggal",
        geo = dict(
            resolution = 50,
            bgcolor= 'rgba(0,0,0,0)',
            scope = 'asia',
            showframe = False,
            showcoastlines = True,
            showland = True,
            landcolor = "#989898",
            countrycolor = "rgb(255, 255, 255)" ,
            coastlinecolor = "rgb(255, 255, 255)",
            projection = dict(
                type = 'mercator',
                scale= 2
            ),
            center = dict(
                lon=98.044117,
                lat=36.058394
            )
        ),
        font = {"size": 9, "color":"White"},
        titlefont = {"size": 20, "color":"White"},
        paper_bgcolor='#303030 ',
        plot_bgcolor='#303030 ',
        width=620,
        height=500,
    )

    fig = go.Figure(layout=layout, data=cases)

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def chinaMap_recovered():

    ch_latest = ds.ch_latest

    ch_latest_grouped = ch_latest.groupby(['Province/State', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    ch_latest_grouped['desc'] = ch_latest_grouped.agg('{0[Province/State]} : {0[Recovered]}'.format, axis=1)
    ch_latest_grouped['size'] = ch_latest_grouped['Recovered'].pow(0.7)

    cases = []
    cases.append(go.Scattergeo(
        lon = ch_latest_grouped['Long'],
        lat = ch_latest_grouped['Lat'],
        hovertext=ch_latest_grouped['desc'],
        marker = dict(
                size = ch_latest_grouped['size'],
                color='green',
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
    ) )

    layout = go.Layout(
        title="Peta China dengan Kasus Pulih",
        geo = dict(
            resolution = 50,
            bgcolor= 'rgba(0,0,0,0)',
            scope = 'asia',
            showframe = False,
            showcoastlines = True,
            showland = True,
            landcolor = "#989898",
            countrycolor = "rgb(255, 255, 255)" ,
            coastlinecolor = "rgb(255, 255, 255)",
            projection = dict(
                type = 'mercator',
                scale= 2
            ),
            center = dict(
                lon=98.044117,
                lat=36.058394
            )
        ),
        font = {"size": 9, "color":"White"},
        titlefont = {"size": 20, "color":"White"},
        paper_bgcolor='#303030 ',
        plot_bgcolor='#303030 ',
        width=620,
        height=500,
    )

    fig = go.Figure(layout=layout, data=cases)

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def chinaMap_active():

    ch_latest = ds.ch_latest

    ch_latest_grouped = ch_latest.groupby(['Province/State', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    ch_latest_grouped['desc'] = ch_latest_grouped.agg('{0[Province/State]} : {0[Active]}'.format, axis=1)
    ch_latest_grouped['size'] = ch_latest_grouped['Active'].pow(1.2)

    cases = []
    cases.append(go.Scattergeo(
        lon = ch_latest_grouped['Long'],
        lat = ch_latest_grouped['Lat'],
        hovertext=ch_latest_grouped['desc'],
        marker = dict(
                size = ch_latest_grouped['size'],
                color='yellow',
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
    ) )

    layout = go.Layout(
        title="Peta China dengan Kasus Aktif",
        geo = dict(
            resolution = 50,
            bgcolor= 'rgba(0,0,0,0)',
            scope = 'asia',
            showframe = False,
            showcoastlines = True,
            showland = True,
            landcolor = "#989898",
            countrycolor = "rgb(255, 255, 255)" ,
            coastlinecolor = "rgb(255, 255, 255)",
            projection = dict(
                type = 'mercator',
                scale= 2
            ),
            center = dict(
                lon=98.044117,
                lat=36.058394
            )
        ),
        font = {"size": 9, "color":"White"},
        titlefont = {"size": 20, "color":"White"},
        paper_bgcolor='#303030 ',
        plot_bgcolor='#303030 ',
        width=620,
        height=500,
    )

    fig = go.Figure(layout=layout, data=cases)

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div





# peringkat 20 besar
def peringkat_20_confirmed():
    ch_latest_grouped = ds.ch_latest_grouped

    fig = px.bar(ch_latest_grouped.sort_values('Confirmed', ascending=False).head(20).sort_values('Confirmed', ascending=True), 
                x="Confirmed", 
                y="Province/State", 
                title='20 Besar Kasus Terkonfirmasi - Covid-19 di China', 
                text='Confirmed', 
                orientation='h', 
                width=500, 
                height=450, 
                range_x = [0, max(ch_latest_grouped['Confirmed'])+10000])

    fig.update_traces(marker_color='#084177', 
                        opacity=0.8, 
                        textposition='outside')

    fig.update_layout(
        titlefont = {"size": 12, "color":"White"},
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_deaths():
    ch_latest_grouped = ds.ch_latest_grouped

    fig = px.bar(ch_latest_grouped.sort_values('Deaths', ascending=False).head(20).sort_values('Deaths', ascending=True), 
                x="Deaths", 
                y="Province/State", 
                title='20 Besar Kasus Meninggal - Covid-19 di China', 
                text='Deaths', 
                orientation='h', 
                width=500, 
                height=450, 
                range_x = [0, max(ch_latest_grouped['Deaths'])+1000])

    fig.update_traces(marker_color='#ff1e56', 
                        opacity=0.8, 
                        textposition='outside')

    fig.update_layout(
        titlefont = {"size": 12, "color":"White"},
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_recovered():
    ch_latest_grouped = ds.ch_latest_grouped

    fig = px.bar(ch_latest_grouped.sort_values('Recovered', ascending=False).head(20).sort_values('Recovered', ascending=True), 
                x="Recovered", 
                y="Province/State", 
                title='20 Besar Kasus Pulih - Covid-19 di China', 
                text='Recovered', 
                orientation='h', 
                width=500, 
                height=450, 
                range_x = [0, max(ch_latest_grouped['Recovered'])+10000])

    fig.update_traces(marker_color='#26E003', 
                        opacity=0.8, 
                        textposition='outside')

    fig.update_layout(
        titlefont = {"size": 12, "color":"White"},
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_active():
    ch_latest_grouped = ds.ch_latest_grouped

    fig = px.bar(ch_latest_grouped.sort_values('Active', ascending=False).head(10).sort_values('Active', ascending=True), 
            x="Active", 
            y="Province/State", 
            title='10 Besar Kasus Aktif - Covid-19 di China Tanggal 02 Juni 2020', 
            text='Active', 
            orientation='h', 
            width=500, 
            height=450, 
            range_x = [0, max(ch_latest_grouped['Active'])+10])

    fig.update_traces(marker_color='#FFFB26', 
                        opacity=0.8, 
                        textposition='outside')

    fig.update_layout(
        titlefont = {"size": 12, "color":"White"},
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div






#Bagian China
def China_graf_confirmed():
    sns.set(rc={'axes.facecolor':'#353535', 
            'figure.facecolor':'#353535', 
            'text.color' : "white", 
            'axes.labelcolor' : "white",
            'xtick.color': 'white',
            'ytick.color': 'white',
            'lines.linewidth': 3})
    
    f_table = ds.f_table
    f_table = f_table[f_table['Country/Region']=='China']

    confirmed_case = f_table.groupby(['Date', 'Country/Region'])['Confirmed'].sum()
    confirmed_case = confirmed_case.reset_index().sort_values(by=['Date', 'Country/Region'])

    g = sns.FacetGrid(confirmed_case, col="Country/Region", hue="Country/Region", 
                    sharey=False)
    g = g.map(plt.plot, "Date", "Confirmed")
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        labelbottom=False)

    plt.savefig('./DjangoPlotlyDash/static/img/China_confirmed_graph.png',
                facecolor='#303030', edgecolor='none'
                )


def China_graf_newcase():
    sns.set(rc={'axes.facecolor':'#353535', 
            'figure.facecolor':'#353535', 
            'text.color' : "white", 
            'axes.labelcolor' : "white",
            'xtick.color': 'white',
            'ytick.color': 'white',
            'lines.linewidth': 3})
    
    f_table = ds.f_table
    f_table = f_table[f_table['Country/Region']=='China']

    new_case = f_table.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']
    new_case = new_case.sum().diff().reset_index()

    mask = new_case['Country/Region'] != new_case['Country/Region'].shift(1)

    new_case.loc[mask, 'Confirmed'] = np.nan
    new_case.loc[mask, 'Deaths'] = np.nan
    new_case.loc[mask, 'Recovered'] = np.nan

    # temp = temp[temp['Confirmed']>100]

    g = sns.FacetGrid(new_case, col="Country/Region", hue="Country/Region", 
                    sharey=False)
    g = g.map(sns.lineplot, "Date", "Confirmed")
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        labelbottom=False)

    plt.savefig('./DjangoPlotlyDash/static/img/China_newCase_graph.png',
                facecolor='#303030', edgecolor='none'
                )




#10 negara bagian dengan total terbanyak
def confirmed_terbanyak():
    flg = ds.ch_latest_grouped
    fig = flg.sort_values('Confirmed', ascending=False).head(10)

    num = range(1,11,1)
    state = fig['Province/State'].to_list()
    nilai = fig['Confirmed'].to_list()

    hasil = zip(num, state, nilai)
    return hasil

def deaths_terbanyak():
    flg = ds.ch_latest_grouped
    fig = flg.sort_values('Deaths', ascending=False).head(10)

    num = range(1,11,1)
    state = fig['Province/State'].to_list()
    nilai = fig['Deaths'].to_list()

    hasil = zip(num, state, nilai)
    return hasil

def recovered_terbanyak():
    flg = ds.ch_latest_grouped
    fig = flg.sort_values('Recovered', ascending=False).head(10)

    num = range(1,11,1)
    state = fig['Province/State'].to_list()
    nilai = fig['Recovered'].to_list()

    hasil = zip(num, state, nilai)
    return hasil

def active_terbanyak():
    flg = ds.ch_latest_grouped
    fig = flg.sort_values('Active', ascending=False).head(10)

    num = range(1,11,1)
    state = fig['Province/State'].to_list()
    nilai = fig['Active'].to_list()

    hasil = zip(num, state, nilai)
    return hasil





# proporsi kasus dengan donuts charts
def proporsi_confirmed():
    data = ds.ch_latest_grouped.sort_values('Confirmed', 
                                        ascending=False).head(10).sort_values('Confirmed', 
                                                                            ascending=True)

    #persiapan data
    province = data.sort_values('Confirmed', ascending=False).head(9)
    province = province['Province/State'].to_list()

    df = ds.ch_latest_grouped.sort_values('Confirmed', ascending=False)
    #the top 9
    df2 = df[:9].copy()
    #others
    new_row = pd.DataFrame(data = {
        'Province/State' : ['others'],
        'Confirmed' : [df['Confirmed'][9:].sum()],
        'Deaths' : [df['Deaths'][9:].sum()],
        'Recovered' : [df['Deaths'][9:].sum()],
        'Active' : [df['Active'][9:].sum()],
    })
    df2 = pd.concat([df2, new_row])

    labels = list(df2['Province/State'])
    values = list(df2['Confirmed'])

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                insidetextorientation='radial', hole=.3
                                )])
    fig.update_layout(
        legend=dict(
            bgcolor='#353535',
            bordercolor='rgba(255, 255, 255, 0)',
            font = {"size": 9, "color":"White"},
        ),
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        width=780,
        height=400,
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def proporsi_deaths():
    data = ds.ch_latest_grouped.sort_values('Deaths', 
                                        ascending=False).head(10).sort_values('Deaths', 
                                                                            ascending=True)

    #persiapan data
    province = data.sort_values('Deaths', ascending=False).head(9)
    province = province['Province/State'].to_list()

    df = ds.ch_latest_grouped.sort_values('Deaths', ascending=False)
    #the top 9
    df2 = df[:9].copy()
    #others
    new_row = pd.DataFrame(data = {
        'Province/State' : ['others'],
        'Confirmed' : [df['Confirmed'][9:].sum()],
        'Deaths' : [df['Deaths'][9:].sum()],
        'Recovered' : [df['Deaths'][9:].sum()],
        'Active' : [df['Active'][9:].sum()],
    })
    df2 = pd.concat([df2, new_row])

    labels = list(df2['Province/State'])
    values = list(df2['Deaths'])

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                insidetextorientation='radial', hole=.3
                                )])
    fig.update_layout(
        legend=dict(
            bgcolor='#353535',
            bordercolor='rgba(255, 255, 255, 0)',
            font = {"size": 9, "color":"White"},
        ),
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        width=780,
        height=400,
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def proporsi_recovered():
    data = ds.ch_latest_grouped.sort_values('Recovered', 
                                        ascending=False).head(10).sort_values('Recovered', 
                                                                            ascending=True)

    #persiapan data
    province = data.sort_values('Recovered', ascending=False).head(9)
    province = province['Province/State'].to_list()

    df = ds.ch_latest_grouped.sort_values('Recovered', ascending=False)
    #the top 9
    df2 = df[:9].copy()
    #others
    new_row = pd.DataFrame(data = {
        'Province/State' : ['others'],
        'Confirmed' : [df['Confirmed'][9:].sum()],
        'Deaths' : [df['Deaths'][9:].sum()],
        'Recovered' : [df['Deaths'][9:].sum()],
        'Active' : [df['Active'][9:].sum()],
    })
    df2 = pd.concat([df2, new_row])

    labels = list(df2['Province/State'])
    values = list(df2['Recovered'])

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                insidetextorientation='radial', hole=.3
                                )])
    fig.update_layout(
        legend=dict(
            bgcolor='#353535',
            bordercolor='rgba(255, 255, 255, 0)',
            font = {"size": 9, "color":"White"},
        ),
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        width=780,
        height=400,
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def proporsi_active():
    data = ds.ch_latest_grouped.sort_values('Active', 
                                        ascending=False).head(10).sort_values('Active', 
                                                                            ascending=True)

    #persiapan data
    province = data.sort_values('Active', ascending=False).head(9)
    province = province['Province/State'].to_list()

    df = ds.ch_latest_grouped.sort_values('Active', ascending=False)
    #the top 9
    df2 = df[:9].copy()
    #others
    new_row = pd.DataFrame(data = {
        'Province/State' : ['others'],
        'Confirmed' : [df['Confirmed'][9:].sum()],
        'Deaths' : [df['Deaths'][9:].sum()],
        'Recovered' : [df['Deaths'][9:].sum()],
        'Active' : [df['Active'][9:].sum()],
    })
    df2 = pd.concat([df2, new_row])

    labels = list(df2['Province/State'])
    values = list(df2['Active'])

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                insidetextorientation='radial', hole=.3
                                )])
    fig.update_layout(
        legend=dict(
            bgcolor='#353535',
            bordercolor='rgba(255, 255, 255, 0)',
            font = {"size": 9, "color":"White"},
        ),
        font = {"size": 8, "color":"White"},
        paper_bgcolor='#303030',
        width=780,
        height=400,
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div





#Total kasus saat ini
def jumlah_terkini_c():
    flg = ds.ch_latest_grouped
    temp = flg['Confirmed'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_d():
    flg = ds.ch_latest_grouped
    temp = flg['Deaths'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_r():
    flg = ds.ch_latest_grouped
    temp = flg['Recovered'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_a():
    flg = ds.ch_latest_grouped
    temp = flg['Active'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_negara_bagian():
    hasil = ds.ch_latest_grouped.sort_values(by='Confirmed', ascending=False).reset_index(drop=True)
    temp = hasil['Province/State'].count()
    return temp