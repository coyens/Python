import requests
import pandas
import datetime

#params
radius = '50'
types_POI = 'pharmacy'
# Only one type may be specified#
# https://developers.google.com/places/web-service/supported_types
API_key = 'AIzaSyAmhFBRve-kNGL3rSUcRG3MSijPel62WMg'

def POI_search(latlong):
    station_list = []
    station_list2 = []
    station_list3 = []
    url ='https://maps.googleapis.com/maps/api/place/search/json?location={latlong}&radius={radius}&types={types_POI}&sensor=false&key={API_key}'
    response = requests.get(url).json()
    #print(response.status_code)
    station_list = response['results']
    if response.get('next_page_token') == None:  
        pass
       #print ('koniec')
    else:
        token = response['next_page_token']
        url = 'https://maps.googleapis.com/maps/api/place/search/json?location={latlong}&radius={radius}&types={types_POI}&sensor=false&key={API_key}'
        response2 = requests.get(url2).json()
        station_list2 = response2['results']
        if response2.get('next_page_token') == None:  
            pass #print ('koniec')
        else:
            token2 = response2['next_page_token']
            url = f'https://maps.googleapis.com/maps/api/place/search/json?location={latlong}&radius={radius}&types={types_POI}&sensor=false&key={API_key}'
            response3 = requests.get(url3).json()
            station_list3 = response3['results']

    station_list = station_list + station_list2 + station_list3
    return len(station_list)
        


plik2 = 'latlong.csv'
plik3 = 'dk_restaurant.csv'
plik4= 'dk_shop.csv'

def open_CSV(plik3):
    gps_df = pandas.read_csv(plik3,encoding='utf-8-sig', sep = ',')
    gps_df.iloc[:,0] = gps_df.iloc[:,0].astype(str)
    gps_df['latlong'] = gps_df.iloc[:,1].astype(str) + ', ' + gps_df.iloc[:,2].astype(str)
    return gps_df
    

#gps_df['nr_restaurants'] = gps_df['latlong'].apply(POI_search)
    
def pd_to_csv(pd_DF, file_name): #zapisuje DataFrame do csv, format nazwy najlepiej "MARKA_KodKraju" np. "Orlen_PL"
    z = str(datetime.datetime.now())
    date_now = z[:10]+'_'+z[11:13]+z[14:16]
    fname = date_now+'_'+file_name+'.csv'
    pd_DF = pd_DF.drop(columns=['latlong'])
    return pd_DF.to_csv(fname, encoding='utf-8-sig', sep = '$')

#pd_to_csv(gps_df, 'dk_restaurant_500')
    


API_keyasd = '54.8598490	9.3614410'
print(POI_search(asd))

gps_df = open_CSV(plik3)
gps_df['nr_restaurants'] = gps_df['latlong'].apply(POI_search)
pd_to_csv(gps_df, 'dk_restaurant_500_top150')
