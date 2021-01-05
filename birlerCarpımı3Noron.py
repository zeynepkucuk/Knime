#!/usr/bin/env python
#-*- coding: utf8 -*-
import math

egiticiler = [0,1,2,3,5,7,8,10]

testciler = [4,6,9]

hedefler = [0,1,2,3,5,7,8,10]

istenenler = [4,6,9]

o_ks = 0.6

esik_agirlik = [0.25, 0.35, 0.45, 0.55]

acceptable_total_error = 0.014

acceptable_single_error = 0.009

A_weigths = [-0.75, 0.75]

B_weigths = [-0.55, 0.55]

C_weigths = [-0.25, 0.25]

D_weigths = [-0.35, 0.55, 0.35]



def ileri_besleme(ipt1,ipt2,w1,w2,ed):
    sum = ((ipt1 * w1) + (ipt2 * w2) + (1.0 * ed))
    return float(sum)

def normalize (x):
    a = x /10
    return float(a)

def denormalize (y): 
    a = 100*y
    return float(a)

def sigmoid_function(x):
    deger = (1)/(1 + (math.exp(-x)))
    return float(deger)

def purelin (sonuc):
    return float(sonuc)

def tanjanthiperbolik_function(u):
    a = math.exp(u)
    b = math.exp(u)    
    return float((a-b)/(a+b))

def agirlik_guncelle(old_w,delta, ipt):
    new_w = old_w + (o_ks * delta * ipt)
    return float(new_w)

def Katman_dugum_hesapla(ipt1,ipt2,w1,w2,ed):
    NET = ileri_besleme(ipt1,ipt2,w1,w2,ed)
    return float(NET)

def sigmoid_turev_function(x):   
    return ((1) - x)

def purelin_turev(x):
    return x


def tanjanthiperbolik_turev_function(u):
    a = math.exp(u)
    b = math.exp(-u)               
    return float(4/((a+b)**2))

def mean_square_error(liste):    
    toplam = 0.0
    adim = 0
    while adim < 8 : 
        toplam += ((liste[adim]) ** 2)
        adim += 1
        
    ortalama_hata = math.sqrt(toplam / 8)
    return ortalama_hata  

epoch = 0
while epoch <500:

    epoch_error_list = []
    uretilen_sonuc_list = []
    iterasyon = 0

    while iterasyon < 8:
        
        KTM0 = float(Katman_dugum_hesapla(float(normalize(1)), float(normalize(egiticiler[iterasyon])), float(A_weigths[0]),float(A_weigths[1]), float(esik_agirlik[0])))
        KTM1 = float(Katman_dugum_hesapla(float(normalize(1)),float(normalize(egiticiler[iterasyon])),float(B_weigths[0]),float(B_weigths[1]), float(esik_agirlik[1])))
        KTM2 = float(Katman_dugum_hesapla(float(normalize(1)), float(normalize(egiticiler[iterasyon])), float(C_weigths[0]),float(C_weigths[1]), float(esik_agirlik[2])))

        F0 = float(tanjanthiperbolik_function(float(KTM0)))# ilk katman ileri beslemede tanjanthiperbolik fonksiyonunu kullanilmasi
        F1 = float(tanjanthiperbolik_function(float(KTM1)))
        F2 = float(tanjanthiperbolik_function(float(KTM2)))

        #F0 = float(sigmoid_function(KTM0))
        #F1 = float(sigmoid_function(KTM1)) *********Tercihe bagli kullanma icin logaritmik sigmoid fonksiyon
        #F2 = float(sigmoid_function(KTM2))

        KTM3 = float(float(F0) * float(D_weigths[0]) + (float(F1) * float(D_weigths[1])) + (float(F2) * float(D_weigths[2])) +  (1.0 * float(esik_agirlik[3])))
        
        cikan_sonuc = sigmoid_function(float(KTM3)) #cikis katmaninda logaritmik sigmoid fonksiyon kullanilmasi
        
        #cikan_sonuc = float(purelin(KTM3)) #********Tercih edilmesi halinde Lineer Purelin fonksiyonu kullanilabilir

        e = (float(normalize(hedefler[iterasyon])) - float(cikan_sonuc))

        print ("e = ", e)
        
        if e != 0:
            
            #----------------------Hatanin cikis katmaninin girdisine  aksettirilmesi-------------------
            delta3 = float((cikan_sonuc * sigmoid_turev_function(KTM3) * e))  #***** cikis katmaninda logaritmik Sigmoid fonksiyon kullanildiginden geri yayilimda onun turevinin kullanilmasi
            #delta3 = cikan_sonuc * purelin_turev_fuction(KTM3) #******* cikis katmaninda purelin fonksiyonu tercih edilirse geri yayilimda onun turevi kullanilmalidir
            

            #----------------------Hatanin cikiş katmaninin girdi agirliklarina ve esik degerine yansitilmasi----------
            new_DW_0 = agirlik_guncelle(float(D_weigths[0]), float(delta3), F0)

            new_DW_1 = agirlik_guncelle(float(D_weigths[1]), float(delta3), F1)
            
            new_DW_2 = agirlik_guncelle(float(D_weigths[2]), float(delta3), F2)
            
            new_ED_3 = agirlik_guncelle(float(esik_agirlik[3]), float(delta3), 1)


            #---------------------Hatanin gizli katman girdilerine aksettirilmesi----------------------------------------
            
            delta0 = float((F0) * (tanjanthiperbolik_turev_function(F0)) * (delta3 * D_weigths[0])) #ilk katmanda kullanilan fonksiyonun turevinin geri yayilimda kullanilmasi
            #delta0 =  F0 * sigmoid_turev_function(F0) * delta3 * D_weigths[0]  ***** ilk katmanda logaritmik Sigmoid fonksiyon kullanilmasi halinde geri yayilimda onun turevinin kullanilmasi gerekir
            
            delta1 = float((F1) * (tanjanthiperbolik_turev_function(F1)) * (delta3 * D_weigths[1])) #ilk katmanda kullanilan fonksiyonun turevinin geri yayilimda kullanilmasi
            #delta1 =  F1 * sigmoid_turev_function(F1)*delta3 * D_weigths[1]  ***** ilk katmanda logaritmik Sigmoid fonksiyon kullanilmasi halinde geri yayilimda onun turevinin kullanilmasi gerekir

            delta2 =  (F2) * (tanjanthiperbolik_turev_function(F2)) * (delta3 * D_weigths[2]) #ilk katmanda kullanilan fonksiyonun turevinin geri yayilimda kullanilmasi
            #delta2 =  F2 * sigmoid_turev_function(F2) * delta3 * hird_weigths[2]  #***** ilk katmanda logaritmik Sigmoid fonksiyon kullanilmasi halinde geri yayilimda onun turevinin kullanilmasi gerekir



            #----------------Cikis katmani girdi agirliklarinin hata dagitimiyla hesaplanan yeni degerlerinin guncellenmesi---------
            D_weigths[0] = float(new_DW_0)
            print (" agirlik 3-0 ", D_weigths[0])

            D_weigths[1] = float(new_DW_1)
            print (" agirlik 3-1 ", D_weigths[1] )             

            D_weigths[2] = float(new_DW_2)
            print (" agirlik 3-2 ", D_weigths[2])
            

            esik_agirlik[3] =  float(new_ED_3)
            print (" esik 3-3 ", esik_agirlik[3])

            
            #-------------- Hatanin gizli katman girdilerinin agirliklarina ve esik degerlerine yansitilip hesaplanan yeni degerlerin guncellenmesi ------
            
            new_AW_0 = agirlik_guncelle(A_weigths[0], float(delta0), float(normalize(1)))
            A_weigths[0] = float(new_AW_0)
            print (" agirlik 1-12 ", A_weigths[0])
            
            new_AW_1 = agirlik_guncelle(A_weigths[1],float(delta0), float(normalize(egiticiler[iterasyon])))
            A_weigths[1] = float(new_AW_1)
            print (" agirlik 1-22 ", float(A_weigths[1]))

            
            new_BW_0 = agirlik_guncelle(B_weigths[0], float(delta1), float(normalize(1)))
            B_weigths[0] = float(new_BW_0)
            print (" agirlik 2-12 ", B_weigths[0])
            
            new_BW_1 = agirlik_guncelle(B_weigths[1],float(delta1), float(normalize(egiticiler[iterasyon])))
            B_weigths[1] = float(new_BW_1)
            print (" agirlik 2-22 ", B_weigths[1])


            new_CW_0 = agirlik_guncelle(C_weigths[0], float(delta2), float(normalize(1)))
            C_weigths[0] = float(new_CW_0)
            print (" agirlik 2-12 ", C_weigths[0])
            
            new_CW_1 = agirlik_guncelle(C_weigths[1],float(delta2), float(normalize(egiticiler[iterasyon])))
            C_weigths[1] = float(new_CW_1)
            print (" agirlik 2-22 ", C_weigths[1])

            new_ED_0 = agirlik_guncelle(esik_agirlik[0], float(delta0), 1)
            esik_agirlik[0] = float(new_ED_0)
            print (" esik0 ",  esik_agirlik[0])

            new_ED_1 = agirlik_guncelle(esik_agirlik[1], float(delta1), 1)
            esik_agirlik[0] = float(new_ED_1)
            print (" esik1 ",  esik_agirlik[1])
           
            new_ED_2 = agirlik_guncelle(esik_agirlik[2], float(delta2), 1)
            esik_agirlik[2] = float(new_ED_2)
            print (" esik2 ",  esik_agirlik[2])



            
        epoch_error_list.append(e)
        uretilen_sonuc_list.append(denormalize(cikan_sonuc))
        print ("Iterasyon Hatasi = ", cikan_sonuc , "\n")
        print (" Iterasyon", iterasyon)
        iterasyon += 1
       
    epoch_mean_error = float(mean_square_error(epoch_error_list))
    
    print ("Epoch hata listesi = ", epoch_error_list)
    
    print ("Epoch ortalama hatasi = ", epoch_mean_error)
    
    if epoch_mean_error > acceptable_total_error:
        print (" Epoch ", epoch)
        #o_ks = o_ks*0.7
        #print " Ogrenme kaysayisi ", o_ks
        epoch +=1
        
    else:
        print (epoch, ". epoch sonucunda eğitim tamamlanmıştır. Test işlemleri başlamıştır. \n")
test = 0
while test < 3:


    KTM0 = float(Katman_dugum_hesapla(float(normalize(1)), float(normalize(testciler[test])), float(A_weigths[0]),float(A_weigths[1]), float(esik_agirlik[0])))
    KTM1 = float(Katman_dugum_hesapla(float(normalize(1)),float(normalize(testciler[test])),float(B_weigths[0]),float(B_weigths[1]), float(esik_agirlik[1])))
    KTM2 = float(Katman_dugum_hesapla(float(normalize(1)), float(normalize(testciler[test])), float(C_weigths[0]),float(C_weigths[1]), float(esik_agirlik[2])))

    #F0 = float(sigmoid_function(KTM0))
    #F1 = float(sigmoid_function(KTM1))
    #F2 = float(sigmoid_function(KTM2))

    F0 = float(tanjanthiperbolik_function(float(KTM0)))# ilk katman ileri beslemede tanjanthiperbolik fonksiyonunu kullanilmasi
    F1 = float(tanjanthiperbolik_function(float(KTM1)))
    F2 = float(tanjanthiperbolik_function(float(KTM2)))
               
    KTM3 = float((float(F0) * float(D_weigths[0])) + (float(F1) * float(D_weigths[1])) + (float(F2) * float(D_weigths[2])) +  (1.0 * float(esik_agirlik[3])))
    cikan_sonuc = float(sigmoid_function(KTM3)) 


    print (" cikan_sonuc = ", cikan_sonuc)
    test_error = (normalize(istenenler[test]) - cikan_sonuc)

    if test_error <= acceptable_single_error :

        print  (1, " x ", testciler[test], " = ", denormalize(cikan_sonuc), "  Test isleminin  ", test, ".  islemi basarili oldu." )

    elif denormalize(testciler[test]) == denormalize(cikan_sonuc):

        print  (1, " x ", testciler[test], " = ", denormalize(cikan_sonuc), "  Test isleminin  ", test,  ".  islemi  dogru sonuc ve  buyuk  hata verdi.")

    else:

        print  (1, " x ", testciler[test], " = ", denormalize(cikan_sonuc), "  Test isleminin  ", test,  ".  islemi  yanlis  sonuc ve buyuk hata verdi .")  


    test += 1 
