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

def worldMap_confirmed():
    f_latest_grouped = ds.f_latest_grouped

    fig = px.choropleth(f_latest_grouped, locations="Country/Region",
                        locationmode='country names', color=np.log(f_latest_grouped["Confirmed"]),
                        hover_name="Country/Region", hover_data=['Confirmed'],
                        color_continuous_scale="Viridis",
                        title='Negara Dengan Kasus Terkonfirmasi',
                        width=500, height=350)

    fig.update(layout_coloraxis_showscale=True)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        geo=dict(bgcolor= '#2973C8'),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def worldMap_Deaths():
    f_latest_grouped = ds.f_latest_grouped

    temp = f_latest_grouped[f_latest_grouped['Deaths']>0]

    fig = px.choropleth(temp, 
                    locations="Country/Region", locationmode='country names',
                    color=np.log(temp["Deaths"]), hover_name="Country/Region", 
                    color_continuous_scale="Peach", hover_data=['Deaths'],
                    title='Negara Dengan Kasus Meninggal Dunia',
                    width=500, height=350)

    fig.update(layout_coloraxis_showscale=True)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        geo=dict(bgcolor= '#2973C8'),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def worldMap_Recovered():
    f_latest_grouped = ds.f_latest_grouped

    temp = f_latest_grouped[f_latest_grouped['Recovered']>0]

    fig = px.choropleth(temp, 
                    locations="Country/Region", 
                    locationmode='country names',
                    color=np.log(temp["Recovered"]), 
                    hover_name="Country/Region", 
                    color_continuous_scale=px.colors.sequential.Greens, 
                    hover_data=['Recovered'],
                    title='Negara Dengan Kasus Pulih',
                    width=500, height=350)

    fig.update(layout_coloraxis_showscale=True)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        geo=dict(bgcolor= '#2973C8'),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div

def worldMap_Active():
    f_latest_grouped = ds.f_latest_grouped

    temp = f_latest_grouped[f_latest_grouped['Active']>0]

    fig = px.choropleth(temp, 
                    locations="Country/Region", 
                    locationmode='country names',
                    color=np.log(temp["Active"]), 
                    hover_name="Country/Region", 
                    color_continuous_scale=px.colors.sequential.YlOrBr, 
                    hover_data=['Active'],
                    title='Negara Dengan Kasus Aktif',
                    width=500, height=350)

    fig.update(layout_coloraxis_showscale=True)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        geo=dict(bgcolor= '#2973C8'),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%', output_type='div', include_plotlyjs=False)
    return plot_div




#Grafik Kasus Terkonfirmasi
def graf_confirmed():
    sns.set(rc={'axes.facecolor':'#353535', 
            'figure.facecolor':'#353535', 
            'text.color' : "white", 
            'axes.labelcolor' : "white",
            'xtick.color': 'white',
            'ytick.color': 'white',
            'lines.linewidth': 3})
    
    #tampilkan 10 kota dengan kasus konfirmasi terbanyak
    flg = ds.f_latest_grouped
    country = flg.sort_values('Confirmed', ascending=False).head(10)
    country = country['Country/Region'].to_list()
    
    f_table = ds.f_table
    f_table = f_table[f_table['Country/Region'].isin(country)]

    confirmed_case = f_table.groupby(['Date', 'Country/Region'])['Confirmed'].sum()
    confirmed_case = confirmed_case.reset_index().sort_values(by=['Date', 'Country/Region'])

    g = sns.FacetGrid(confirmed_case, col="Country/Region", hue="Country/Region", 
                    sharey=False, col_wrap=3)
    g = g.map(plt.plot, "Date", "Confirmed")
    
    plt.savefig('./DjangoPlotlyDash/static/img/10_bigest_confirmed_graph.png',
                facecolor='#303030', edgecolor='none'
                )




#Bagian Indonesia
def indo_graf_confirmed():
    sns.set(rc={'axes.facecolor':'#353535', 
            'figure.facecolor':'#353535', 
            'text.color' : "white", 
            'axes.labelcolor' : "white",
            'xtick.color': 'white',
            'ytick.color': 'white',
            'lines.linewidth': 3})
    
    f_table = ds.f_table
    f_table = f_table[f_table['Country/Region']=='Indonesia']

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

    plt.savefig('./DjangoPlotlyDash/static/img/Indonesia_confirmed_graph.png',
                facecolor='#303030', edgecolor='none'
                )


def indo_graf_newcase():
    sns.set(rc={'axes.facecolor':'#353535', 
            'figure.facecolor':'#353535', 
            'text.color' : "white", 
            'axes.labelcolor' : "white",
            'xtick.color': 'white',
            'ytick.color': 'white',
            'lines.linewidth': 3})
    
    f_table = ds.f_table
    f_table = f_table[f_table['Country/Region']=='Indonesia']

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

    plt.savefig('./DjangoPlotlyDash/static/img/Indonesia_newCase_graph.png',
                facecolor='#303030', edgecolor='none'
                )




# peringkat 20 besar
def peringkat_20_confirmed():
    flg = ds.f_latest_grouped
    fig = px.bar(flg.sort_values('Confirmed', ascending=False).head(20).sort_values('Confirmed', ascending=True), 
            x="Confirmed", y="Country/Region", text='Confirmed', orientation='h', 
            width=550, height=500, range_x = [0, max(flg['Confirmed'])+500000])
    fig.update_traces(marker_color='#084177', opacity=0.8, textposition='outside')

    fig.update_layout(
        title='20 Negara Dengan Kasus Terkonfirmasi Terbanyak',
        titlefont = {"size": 14, "color":"White"},
        font = {"size": 10, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_deaths():
    flg = ds.f_latest_grouped
    fig = px.bar(flg.sort_values('Deaths', ascending=False).head(20).sort_values('Deaths', ascending=True), 
            x="Deaths", y="Country/Region", title='Deaths Cases', text='Deaths', orientation='h', 
            width=550, height=500, range_x = [0, max(flg['Deaths'])+20000])
    fig.update_traces(marker_color='#ff1e56', opacity=0.8, textposition='outside')

    fig.update_layout(
        title='20 Negara Dengan Kasus Meninggal Dunia Terbanyak',
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_recovered():
    flg = ds.f_latest_grouped
    fig = px.bar(flg.sort_values('Recovered', ascending=False).head(20).sort_values('Recovered', ascending=True), 
            x="Recovered", y="Country/Region", title='Recovered Cases', text='Recovered', orientation='h', 
            width=550, height=500, range_x = [0, max(flg['Recovered'])+300000])
    fig.update_traces(marker_color='#187F01', opacity=0.8, textposition='outside')

    fig.update_layout(
        title='20 Negara Dengan Kasus Pulih Terbanyak',
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def peringkat_20_active():
    flg = ds.f_latest_grouped
    fig = px.bar(flg.sort_values('Active', ascending=False).head(20).sort_values('Active', ascending=True), 
            x="Active", y="Country/Region", title='Active Cases', text='Active', orientation='h', 
            width=550, height=500, range_x = [0, max(flg['Active'])+500000])

    fig.update_traces(marker_color='#f8b400', opacity=0.8, textposition='outside')

    fig.update_layout(
        title='20 Negara Dengan Kasus Aktif Terbanyak',
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 12, "color":"White"},
        paper_bgcolor='#303030',
        plot_bgcolor='#303030',
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div




#10 negara dengan total terbanyak
def confirmed_terbanyak():
    flg = ds.f_latest_grouped
    fig = flg.sort_values('Confirmed', ascending=False).head(10)

    num = range(1,11,1)
    country = fig['Country/Region'].to_list()
    nilai = fig['Confirmed'].to_list()

    hasil = zip(num, country, nilai)
    return hasil

def deaths_terbanyak():
    flg = ds.f_latest_grouped
    fig = flg.sort_values('Deaths', ascending=False).head(10)

    num = range(1,11,1)
    country = fig['Country/Region'].to_list()
    nilai = fig['Deaths'].to_list()

    hasil = zip(num, country, nilai)
    return hasil

def recovered_terbanyak():
    flg = ds.f_latest_grouped
    fig = flg.sort_values('Recovered', ascending=False).head(10)

    num = range(1,11,1)
    country = fig['Country/Region'].to_list()
    nilai = fig['Recovered'].to_list()

    hasil = zip(num, country, nilai)
    return hasil

def active_terbanyak():
    flg = ds.f_latest_grouped
    fig = flg.sort_values('Active', ascending=False).head(10)

    num = range(1,11,1)
    country = fig['Country/Region'].to_list()
    nilai = fig['Active'].to_list()

    hasil = zip(num, country, nilai)
    return hasil





#Total kasus saat ini
def jumlah_terkini_c():
    flg = ds.f_latest_grouped
    temp = flg['Confirmed'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_d():
    flg = ds.f_latest_grouped
    temp = flg['Deaths'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_r():
    flg = ds.f_latest_grouped
    temp = flg['Recovered'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def jumlah_terkini_a():
    flg = ds.f_latest_grouped
    temp = flg['Active'].sum()
    temp = '{:,}'.format(temp).replace(',', '.')
    return temp

def latest_date():
    ft = ds.f_table
    date = ft['Date'].max()
    return date


#-----------------------------------------------------------------------

def world_perkembangan_persebaran():
    formated_gdf = ds.f_table.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered'].max()
    formated_gdf = formated_gdf.reset_index()
    formated_gdf['Date'] = pd.to_datetime(formated_gdf['Date'])
    formated_gdf['Date'] = formated_gdf['Date'].dt.strftime('%m/%d/%Y')
    formated_gdf['size'] = formated_gdf['Confirmed'].pow(0.3)

    fig = px.scatter_geo(formated_gdf, locations="Country/Region", locationmode='country names', 
                        color="Confirmed", size='size', hover_name="Country/Region", 
                        range_color= [0, max(formated_gdf['Confirmed'])+2], 
                        projection="orthographic", animation_frame="Date", 
                        width=400, height=500)

    fig.update(layout_coloraxis_showscale=False)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 8, "color":"White"},
        geo=dict(
            bgcolor= '#303030',
            showocean=True, 
            oceancolor="LightBlue",
        ),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div

def world_perkembangan_persebaran_02():
    formated_gdf = ds.f_table.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered'].max()
    formated_gdf = formated_gdf.reset_index()
    formated_gdf['Date'] = pd.to_datetime(formated_gdf['Date'])
    formated_gdf['Date'] = formated_gdf['Date'].dt.strftime('%m/%d/%Y')
    formated_gdf['size'] = formated_gdf['Confirmed'].pow(0.3)
    
    fig = px.scatter_geo(formated_gdf, locations="Country/Region", locationmode='country names', 
                        color="Confirmed", size='size', hover_name="Country/Region", 
                        range_color= [0, max(formated_gdf['Confirmed'])+2], 
                        projection="natural earth", animation_frame="Date", 
                        width=400, height=500)

    fig.update(layout_coloraxis_showscale=False)

    fig.update_layout(
        titlefont = {"size": 18, "color":"White"},
        font = {"size": 8, "color":"White"},
        geo=dict(
            bgcolor= '#303030',
            showocean=True, 
            oceancolor="LightBlue",
        ),
        paper_bgcolor='#303030'
    )

    plot_div = plot(fig, image_width='100%', image_height='100%',output_type='div', include_plotlyjs=False)
    return plot_div