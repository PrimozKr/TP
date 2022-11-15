def emso_leta_preracun():
    import datetime
    leto= datetime.date.today().year
    
    
    emso=input("Vnesite svojo EMSO stevilko:")
    

    
    if len(emso)== 13:
        print("Vaša EMŠO Stevilka je :",emso)
        
        letnica_rojstva=emso[4:7]
        if letnica_rojstva[0]=='9':
            letnica='1'+letnica_rojstva

        else:
            letnica='2'+ letnica_rojstva

       
        print("letnica rojstva je:",letnica)
        letnica=int(letnica)

        starost =leto  - letnica
        print("stari ste",starost,"let")
            
        
              
         

    elif len(emso)<13:
        print("Vnesli ste premalo števil - Vnesti morate 13 mestno stevilko");
        quit()

    else:
        print("Vnesli ste preveč števil - Vnesti morate 13 mestno stevilko");
        quit()


    
    

emso_leta_preracun ()



