data = {'prices': [41970, 40721, 41197, 41137, 43033],
        'volume': [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

  

def najvecja_vrednost( data ):
    
    
    vrednosti_prices =data['prices']
    vrednosti_volume=data['volume']



    max_prices=max(vrednosti_prices)
    max_volume=max(vrednosti_volume)


    print("Najvecja vrednost kljuca 'prices:" ,max_prices,"\n","najvecja vrednost kljuca ' volume':",max_volume)
  

najvecja_vrednost(data)