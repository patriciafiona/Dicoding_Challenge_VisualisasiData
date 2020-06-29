from django.shortcuts import render
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
#import kaggle
from newsapi import NewsApiClient 
import urllib
from django.conf import settings

#import data
from home.dash_apps.finished_apps import world_sector
from home.dash_apps.finished_apps import US_sector
from home.dash_apps.finished_apps import brazil_sector
from home.dash_apps.finished_apps import china_sector


# Create your views here.
def home(request):
    try:
        #tarik data dari kaggle
        #kaggle.api.authenticate()
        #kaggle.api.dataset_download_files('sudalairajkumar/novel-corona-virus-2019-dataset')

        #ambil berita dari API os.environ['MONGO_API_KEY']
        newsapi = NewsApiClient(api_key = settings.NEWSAPI_API_KEY) 
        top = newsapi.get_top_headlines(
            q='covid-19',
            country='id') 
    
        l = top['articles'] 
        desc =[] 
        news =[] 
        img =[] 
        url=[]
    
        for i in range(len(l)): 
            f = l[i] 
            news.append(f['title']) 
            desc.append(f['description']) 
            img.append(f['urlToImage']) 
            url.append(f['url'])
        mylist = zip(news, desc, img, url) 

        return render(request, 'home/welcome.html', {"mylist":mylist})
        
    except urllib.error.URLError as err: 
        context = {
            'internet_status': False,
            'err_messege': err,
        }
        return render(request, 'home/welcome.html', context)

def world_confirmed(request):

    context = {
        'worldMap_confirmed': world_sector.worldMap_confirmed(),
        'peringkat_20_confirmed': world_sector.peringkat_20_confirmed(),
        'confirmed_terbanyak': world_sector.confirmed_terbanyak(),

        'jumlah_terkini_c': world_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': world_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': world_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': world_sector.jumlah_terkini_a(),
        
        'latest_date': world_sector.latest_date(),

        'graf_confirmed': world_sector.graf_confirmed(),
        'indo_graf_confirmed': world_sector.indo_graf_confirmed(),
        'indo_graf_newcase': world_sector.indo_graf_newcase(),
    }

    return render(request, 'home/world_confirmed.html', context)

def world_deaths(request):
    context = {
        'worldMap_Deaths': world_sector.worldMap_Deaths(),
        'peringkat_20_deaths': world_sector.peringkat_20_deaths(),
        'jumlah_terkini_c': world_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': world_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': world_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': world_sector.jumlah_terkini_a(),

        'latest_date': world_sector.latest_date(),

        'deaths_terbanyak': world_sector.deaths_terbanyak(),
        'graf_confirmed': world_sector.graf_confirmed(),
        'indo_graf_confirmed': world_sector.indo_graf_confirmed(),
        'indo_graf_newcase': world_sector.indo_graf_newcase(),
    }

    return render(request, 'home/world_deaths.html', context)

def world_recovered(request):
    context = {
        'worldMap_Recovered': world_sector.worldMap_Recovered(),
        'peringkat_20_recovered': world_sector.peringkat_20_recovered(),
        'recovered_terbanyak': world_sector.recovered_terbanyak(),

        'jumlah_terkini_c': world_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': world_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': world_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': world_sector.jumlah_terkini_a(),

        'latest_date': world_sector.latest_date(),

        'graf_confirmed': world_sector.graf_confirmed(),
        'indo_graf_confirmed': world_sector.indo_graf_confirmed(),
        'indo_graf_newcase': world_sector.indo_graf_newcase(),
    }

    return render(request, 'home/world_recovered.html', context)

def world_active(request):
    context = {
        'worldMap_Active': world_sector.worldMap_Active(),
        'peringkat_20_active': world_sector.peringkat_20_active(),
        'active_terbanyak': world_sector.active_terbanyak(),

        'jumlah_terkini_c': world_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': world_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': world_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': world_sector.jumlah_terkini_a(),

        'latest_date': world_sector.latest_date(),

        'graf_confirmed': world_sector.graf_confirmed(),
        'indo_graf_confirmed': world_sector.indo_graf_confirmed(),
        'indo_graf_newcase': world_sector.indo_graf_newcase(),
    }

    return render(request, 'home/world_active.html', context)

def world_perkembangan_persebaran(request):
    context = {
        'world_perkembangan_persebaran': world_sector.world_perkembangan_persebaran(),
        'world_perkembangan_persebaran_02': world_sector.world_perkembangan_persebaran_02(),
    }

    return render(request, 'home/world_perkembangan_persebaran.html', context)

#------------------------------------------------------------------------------------------------

def us_confirmed(request):
    context = {
        'us_Map_confirmed': US_sector.us_Map_confirmed(),
        'confirmed_terbanyak': US_sector.confirmed_terbanyak(),
        'peringkat_20_confirmed': US_sector.peringkat_20_confirmed(),
        'proporsi_confirmed': US_sector.proporsi_confirmed(),

        'jumlah_terkini_c': US_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': US_sector.jumlah_terkini_d(),
        'jumlah_negara_bagian': US_sector.jumlah_negara_bagian(),

        'latest_date': world_sector.latest_date(),

        'us_graf_confirmed': US_sector.us_graf_confirmed(),
        'us_graf_newcase': US_sector.us_graf_newcase(),
    }

    return render(request, 'home/us_confirmed.html', context)

def us_deaths(request):
    context = {
        'us_Map_deaths': US_sector.us_Map_Deaths(),
        'deaths_terbanyak': US_sector.deaths_terbanyak(),
        'peringkat_20_deaths': US_sector.peringkat_20_deaths(),
        'proporsi_deaths': US_sector.proporsi_deaths(),

        'jumlah_terkini_c': US_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': US_sector.jumlah_terkini_d(),
        'jumlah_negara_bagian': US_sector.jumlah_negara_bagian(),

        'latest_date': world_sector.latest_date(),

        'us_graf_confirmed': US_sector.us_graf_confirmed(),
        'us_graf_newcase': US_sector.us_graf_newcase(),
    }

    return render(request, 'home/us_deaths.html', context)

#------------------------------------------------------------------------------------------------

def brazil_confirmed(request):
    context = {
        'brazilMap_confirmed': brazil_sector.brazilMap_confirmed(),
        'peringkat_20_confirmed': brazil_sector.peringkat_20_confirmed(),
        'confirmed_terbanyak': brazil_sector.confirmed_terbanyak(),
        'proporsi_confirmed': brazil_sector.proporsi_confirmed(),

        'br_graf_confirmed': brazil_sector.br_graf_confirmed(),
        'br_graf_newcase': brazil_sector.br_graf_newcase(),

        'jumlah_terkini_c': brazil_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': brazil_sector.jumlah_terkini_d(),
        'jumlah_negara_bagian': brazil_sector.jumlah_negara_bagian(),

        'latest_date': world_sector.latest_date(),
    }

    return render(request, 'home/brazil_confirmed.html', context)

def brazil_deaths(request):
    context = {
        'brazilMap_deaths': brazil_sector.brazilMap_deaths(),
        'peringkat_20_deaths': brazil_sector.peringkat_20_deaths(),
        'deaths_terbanyak': brazil_sector.deaths_terbanyak(),
        'proporsi_deaths': brazil_sector.proporsi_deaths(),

        'br_graf_confirmed': brazil_sector.br_graf_confirmed(),
        'br_graf_newcase': brazil_sector.br_graf_newcase(),

        'jumlah_terkini_c': brazil_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': brazil_sector.jumlah_terkini_d(),
        'jumlah_negara_bagian': brazil_sector.jumlah_negara_bagian(),

        'latest_date': world_sector.latest_date(),
    }

    return render(request, 'home/brazil_deaths.html', context)

#------------------------------------------------------------------------------------------------

def china_confirmed(request):
    context = {
        'chinaMap_confirmed': china_sector.ChinaMap_confirmed(),
        'peringkat_20_confirmed': china_sector.peringkat_20_confirmed(),
        'confirmed_terbanyak': china_sector.confirmed_terbanyak(),
        'proporsi_confirmed': china_sector.proporsi_confirmed(),

        'China_graf_confirmed': china_sector.China_graf_confirmed(),
        'China_graf_newcase': china_sector.China_graf_newcase(),

        'latest_date': world_sector.latest_date(),

        'jumlah_terkini_c': china_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': china_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': china_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': china_sector.jumlah_terkini_a(),
        'jumlah_negara_bagian': china_sector.jumlah_negara_bagian(),
    }

    return render(request, 'home/china_confirmed.html', context)

def china_deaths(request):
    context = {
        'chinaMap_deaths': china_sector.chinaMap_deaths(),
        'peringkat_20_deaths': china_sector.peringkat_20_deaths(),
        'deaths_terbanyak': china_sector.deaths_terbanyak(),

        'China_graf_confirmed': china_sector.China_graf_confirmed(),
        'China_graf_newcase': china_sector.China_graf_newcase(),

        'latest_date': world_sector.latest_date(),

        'jumlah_terkini_c': china_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': china_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': china_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': china_sector.jumlah_terkini_a(),
        'jumlah_negara_bagian': china_sector.jumlah_negara_bagian(),
    }

    return render(request, 'home/china_deaths.html', context)

def china_recovered(request):
    context = {
        'chinaMap_recovered': china_sector.chinaMap_recovered(),
        'peringkat_20_recovered': china_sector.peringkat_20_recovered(),
        'recovered_terbanyak': china_sector.recovered_terbanyak(),

        'China_graf_confirmed': china_sector.China_graf_confirmed(),
        'China_graf_newcase': china_sector.China_graf_newcase(),

        'latest_date': world_sector.latest_date(),

        'jumlah_terkini_c': china_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': china_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': china_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': china_sector.jumlah_terkini_a(),
        'jumlah_negara_bagian': china_sector.jumlah_negara_bagian(),
    }

    return render(request, 'home/china_recovered.html', context)

def china_active(request):
    context = {
        'chinaMap_active': china_sector.chinaMap_active(),
        'peringkat_20_active': china_sector.peringkat_20_active(),
        'active_terbanyak': china_sector.active_terbanyak(),

        'China_graf_confirmed': china_sector.China_graf_confirmed(),
        'China_graf_newcase': china_sector.China_graf_newcase(),

        'latest_date': world_sector.latest_date(),

        'jumlah_terkini_c': china_sector.jumlah_terkini_c(),
        'jumlah_terkini_d': china_sector.jumlah_terkini_d(),
        'jumlah_terkini_r': china_sector.jumlah_terkini_r(),
        'jumlah_terkini_a': china_sector.jumlah_terkini_a(),
        'jumlah_negara_bagian': china_sector.jumlah_negara_bagian(),
    }

    return render(request, 'home/china_active.html', context)