from PyQt5.QtWidgets import *
from mysql.connector import MySQLConnection
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import datetime
import time

class pencere(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        uic.loadUi("pencere.ui",self) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.kaydet()
        self.gecis()

    def gecis(self):
        self.btnnext_page.clicked.connect(self.page) 
        self.btn_corba.clicked.connect(self.a1) 
        self.btn_ara_sicaklar.clicked.connect(self.b1) 
        self.btn_ana_yemekler.clicked.connect(self.c1) 
        self.btn_salatalar.clicked.connect(self.d1) 
        self.btn_icecekler.clicked.connect(self.e1) 
        self.btn_tatlilar.clicked.connect(self.f1)  

    def pencereOlustur(self):
        self.a=pencere1(self.txtad.text(),self.txtsoyad.text())     
        self.b=pencere2(self.txtad.text(),self.txtsoyad.text())    
        self.c=pencere3(self.txtad.text(),self.txtsoyad.text())    
        self.d=pencere4(self.txtad.text(),self.txtsoyad.text())    
        self.e=pencere5(self.txtad.text(),self.txtsoyad.text())       
        self.f=pencere6(self.txtad.text(),self.txtsoyad.text()) 
    
    def page(self):
        self.pencereOlustur() 
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.close() 
            self.a.show()

    def a1(self):
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınızı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.a.show()    
            self.close() 

    def b1(self):        
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.b.show()    
            self.close() 
    def c1(self):        
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.c.show()    
            self.close() 
    def d1(self):        
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.d.show()    
            self.close() 
    def e1(self):        
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.e.show()    
            self.close() 
    def f1(self):                
        self.pencereOlustur()        
        if len(self.txtad.text())<1 or len(self.txtsoyad.text())<1:
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Adınızı ve soyadınıı Boş geçmeyiniz lütfen")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            self.kaydet()
            self.f.show()    
            self.close() 

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()
        
    def db_olustur(self):
        try:       
            sorgu='create database masa_otuzalti'
            self.sorgu_Calistir(sorgu)
            self.config['database']= 'masa_otuzalti' 
        except:
            self.config['database'] = 'masa_otuzalti'

    def tablo_olustur(self):
        try:
            self.tablo_ismi="{}_{}".format(self.txtad.text(),self.txtsoyad.text())
            sorgu1="create table {} (siparis VARCHAR(50), siparis_tipi VARCHAR(50))".format(self.tablo_ismi)
            self.sorgu_Calistir(sorgu1)
        except:
            pass

    def kaydet(self):
        self.db_olustur() 
        self.tablo_olustur() 
    
class pencere1(pencere): 
    def __init__(self,ad,soyad):
        super().__init__()
        self.ad=ad
        self.soyad=soyad  
        uic.loadUi("pencere1.ui",self)
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.liste=[]
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad)
        self.btnnext_page1.clicked.connect(self.page1)                          
        self.n1=pencere2(self.txtad.text(),self.txtsoyad.text())
        self.btnsiparis_ver.clicked.connect(self.siparis_ver)
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.config['database']='masa_otuzalti'
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.btn_cek.clicked.connect(self.cek)
        self.btn_ezogelin.clicked.connect(self.ezogelin)
        self.btn_mantar.clicked.connect(self.mantar)
        self.btn_tarhana.clicked.connect(self.tarhana)
        self.btn_mercimek.clicked.connect(self.mercimek)
        self.btn_kellepaca.clicked.connect(self.kellepaca)
        self.btn_domates.clicked.connect(self.domates)
        self.btn_ayran.clicked.connect(self.ayran)
        self.btn_pirinc.clicked.connect(self.pirinc)
        self.btn_yayla.clicked.connect(self.yayla)
        self.gecis()

    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):
        self.liste.clear() 
        self.txtsiparis.setText("")

    def page1(self):
        self.close() 
        self.n1.show() 

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()
    
    def siparis_ver(self):
        for i in self.liste:
            sorgu2="insert into `{}` (`siparis`,`siparis_tipi`) VALUES('{}','{}')".format(self.tablo_ismi,i,"corba") 
            self.sorgu_Calistir(sorgu2)
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")
           

    def ezogelin(self): 
        self.liste.append("ezogelin corbasi")  
        self.txtsiparis.setText(str(self.liste))        

    def mantar(self):
        self.liste.append("mantar corbasi") 
        self.txtsiparis.setText(str(self.liste))

    def tarhana(self):
        self.liste.append("tarhana corbasi") 
        self.txtsiparis.setText(str(self.liste)) 

    def mercimek(self):
        self.liste.append("mercimek corbasi") 
        self.txtsiparis.setText(str(self.liste)) 

    def kellepaca(self):
        self.liste.append("kellepaca corbasi") 
        self.txtsiparis.setText(str(self.liste))

    def domates(self):
        self.liste.append("domates corbasi") 
        self.txtsiparis.setText(str(self.liste))

    def ayran(self):
        self.liste.append("ayran corbasi") 
        self.txtsiparis.setText(str(self.liste))

    def pirinc(self):
        self.liste.append("pirinc corbasi") 
        self.txtsiparis.setText(str(self.liste))

    def yayla(self):
        self.liste.append("yayla corbasi") 
        self.txtsiparis.setText(str(self.liste))

class pencere2(pencere):
    def __init__(self,ad,soyad): 
        super().__init__()
        uic.loadUi("pencere2.ui",self)
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database'] = 'masa_otuzalti'
        self.btn_cek.clicked.connect(self.cek)
        self.btnnext_page2.clicked.connect(self.page2)
        self.btn_onceki1.clicked.connect(self.onceki1)
        self.btnsiparis_ver.clicked.connect(self.siparis_ver)
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.n2=pencere3(self.txtad.text(),self.txtsoyad.text()) 
        self.liste=[] 
        self.btn_kalamar.clicked.connect(self.kalamar)
        self.btn_hamburger.clicked.connect(self.hamburger)
        self.btn_pizza.clicked.connect(self.pizza)
        self.btn_patates.clicked.connect(self.patates)
        self.btn_nugget.clicked.connect(self.nugget)
        self.btn_sogan.clicked.connect(self.sogan)
        self.btn_sis.clicked.connect(self.sis)
        self.btn_durum.clicked.connect(self.durum)
        self.btn_meze.clicked.connect(self.meze)
        self.gecis()


    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):

        self.liste.clear() 
        self.txtsiparis.setText("")

    def page2(self):
        self.n2.show()
        self.close()

    def onceki1(self):
        self.lat1=pencere1(self.txtad.text(),self.txtsoyad.text())
        self.close()        
        self.lat1.show()

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()
    
    def siparis_ver(self):
        for i in self.liste:
            sorgu3="insert into `{}` (`siparis`,`siparis_tipi`) values('{}','{}')".format(self.tablo_ismi,i,"ara_sicaklar")   
            self.sorgu_Calistir(sorgu3)
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")
     
    def kalamar(self): 
        self.liste.append("kalamar")  
        self.txtsiparis.setText(str(self.liste))   
        
    def hamburger(self):
        self.liste.append("hamburger") 
        self.txtsiparis.setText(str(self.liste))

    def pizza(self):
        self.liste.append("pizza") 
        self.txtsiparis.setText(str(self.liste)) 

    def patates(self):
        self.liste.append("patates") 
        self.txtsiparis.setText(str(self.liste)) 

    def nugget(self):
        self.liste.append("nugget") 
        self.txtsiparis.setText(str(self.liste))

    def sogan(self):
        self.liste.append("sogan halkasi") 
        self.txtsiparis.setText(str(self.liste))

    def sis(self):
        self.liste.append("tavuk_sis") 
        self.txtsiparis.setText(str(self.liste))

    def durum(self):
        self.liste.append("durum") 
        self.txtsiparis.setText(str(self.liste))

    def meze(self):
        self.liste.append("meze") 
        self.txtsiparis.setText(str(self.liste))
       
class pencere3(pencere):
    def __init__(self,ad,soyad):
        super().__init__()
        uic.loadUi("pencere3.ui",self)  
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database']='masa_otuzalti'
        self.btn_cek.clicked.connect(self.cek)
        self.btnnext_page3.clicked.connect(self.page3)
        self.btn_onceki2.clicked.connect(self.onceki2)
        self.btnsiparis_ver.clicked.connect(self.siparis_ver)
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.liste=[] 
        self.n3=pencere4(self.txtad.text(),self.txtsoyad.text())    
        self.btn_kofte.clicked.connect(self.kofte)
        self.btn_tavuk.clicked.connect(self.tavuk)
        self.btn_alinazik.clicked.connect(self.alinazik)
        self.btn_adana.clicked.connect(self.adana)
        self.btn_urfa.clicked.connect(self.urfa)
        self.btn_pilav.clicked.connect(self.pilav)
        self.btn_mercimek_pilavi.clicked.connect(self.mercimek) 
        self.btn_kuru.clicked.connect(self.kuru)
        self.btn_makarna.clicked.connect(self.makarna)
        self.gecis()

    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):
        self.liste.clear() 
        self.txtsiparis.setText("")

    def page3(self): 
        self.n3.show() 
        self.close()

    def onceki2(self):
        self.lat2=pencere2(self.txtad.text(),self.txtsoyad.text())
        self.lat2.show()
        self.close()

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()

    def siparis_ver(self):
        for i in self.liste:           
            sorgu4="insert into `{}` (`siparis`,`siparis_tipi`) values('{}','{}')".format(self.tablo_ismi,i,"ana_yemekler")   
            self.sorgu_Calistir(sorgu4)
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")

    def kofte(self): 
        self.liste.append("kofte")  
        self.txtsiparis.setText(str(self.liste))   


    def tavuk(self):
        self.liste.append("tavuk") 
        self.txtsiparis.setText(str(self.liste))

    def alinazik(self):
        self.liste.append("alinazik") 
        self.txtsiparis.setText(str(self.liste)) 

    def adana(self):
        self.liste.append("adana") 
        self.txtsiparis.setText(str(self.liste)) 

    def urfa(self):
        self.liste.append("urfa") 
        self.txtsiparis.setText(str(self.liste))

    def pilav(self):
        self.liste.append("pilav") 
        self.txtsiparis.setText(str(self.liste))

    def mercimek(self):
        self.liste.append("mercimek") 
        self.txtsiparis.setText(str(self.liste))

    def kuru(self):
        self.liste.append("kuru") 
        self.txtsiparis.setText(str(self.liste))

    def makarna(self):
        self.liste.append("makarna") 
        self.txtsiparis.setText(str(self.liste))

class pencere4(pencere):
    def __init__(self,ad,soyad):
        super().__init__()
        uic.loadUi("pencere4.ui",self) 
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database']='masa_otuzalti'
        self.btn_cek.clicked.connect(self.cek)
        self.btnnext_page4.clicked.connect(self.page4)
        self.btn_onceki3.clicked.connect(self.onceki3)
        self.btnsiparis_ver.clicked.connect(self.siparis_ver)
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.n4=pencere5(self.txtad.text(),self.txtsoyad.text())    
        self.liste=[] 
        self.btn_sezar.clicked.connect(self.sezar)
        self.btn_coban.clicked.connect(self.coban)
        self.btn_mevsim.clicked.connect(self.mevsim)
        self.btn_diyet.clicked.connect(self.diyet)
        self.btn_tavuk.clicked.connect(self.tavuk)
        self.btn_peynirli.clicked.connect(self.peynirli)
        self.btn_balikli.clicked.connect(self.balikli) 
        self.btn_gavur.clicked.connect(self.gavur)
        self.btn_sefin.clicked.connect(self.sefin)
        self.gecis()

    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):
        self.liste.clear() 
        self.txtsiparis.setText("")

    def page4(self):
        self.n4.show()
        self.close()

    def onceki3(self):
        self.lat3=pencere3(self.txtad.text(),self.txtsoyad.text()) 
        self.lat3.show()
        self.close()

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()

    def siparis_ver(self):
        for i in self.liste:
            sorgu2="insert into `{}` (`siparis`,`siparis_tipi`) VALUES('{}','{}')".format(self.tablo_ismi,i,"salatalar") 
            self.sorgu_Calistir(sorgu2) 
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")

    def sezar(self): 
        self.liste.append("sezar salatasi")  
        self.txtsiparis.setText(str(self.liste))   


    def coban(self):
        self.liste.append("coban") 
        self.txtsiparis.setText(str(self.liste))

    def mevsim(self):
        self.liste.append("mevsim") 
        self.txtsiparis.setText(str(self.liste)) 

    def diyet(self):
        self.liste.append("diyet") 
        self.txtsiparis.setText(str(self.liste)) 

    def tavuk(self):
        self.liste.append("tavuk") 
        self.txtsiparis.setText(str(self.liste))

    def peynirli(self):
        self.liste.append("peynirli") 
        self.txtsiparis.setText(str(self.liste))

    def balikli(self):
        self.liste.append("ton balikli") 
        self.txtsiparis.setText(str(self.liste))

    def gavur(self):
        self.liste.append("gavur") 
        self.txtsiparis.setText(str(self.liste))

    def sefin(self):
        self.liste.append("sefin") 
        self.txtsiparis.setText(str(self.liste))

class pencere5(pencere):
    def __init__(self,ad,soyad):
        super().__init__()
        uic.loadUi("pencere5.ui",self)
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database']='masa_otuzalti'
        self.btn_cek.clicked.connect(self.cek)
        self.btnnext_page5.clicked.connect(self.page5)
        self.btn_onceki4.clicked.connect(self.onceki4)
        self.btnsiparis_ver.clicked.connect(self.siparis_ver)
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.n5=pencere6(self.txtad.text(),self.txtsoyad.text())    
        self.liste=[] 
        self.btn_su.clicked.connect(self.su)
        self.btn_kimiz.clicked.connect(self.kimiz)
        self.btn_salgam.clicked.connect(self.salgam)
        self.btn_sari.clicked.connect(self.sari)
        self.btn_siyah.clicked.connect(self.siyah)
        self.btn_ayran.clicked.connect(self.ayran)
        self.btn_cay.clicked.connect(self.cay) 
        self.btn_meyve_suyu.clicked.connect(self.meyve_suyu)
        self.btn_kahve.clicked.connect(self.kahve) 
        self.gecis()

    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):
        self.liste.clear() 
        self.txtsiparis.setText("")

    def page5(self):
        self.n5.show()
        self.close()

    def onceki4(self):
        self.lat4=pencere4(self.txtad.text(),self.txtsoyad.text())
        self.close()
        self.lat4.show()

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()

    def siparis_ver(self):
        for i in self.liste:
            sorgu2="insert into `{}` (`siparis`,`siparis_tipi`) VALUES('{}','{}')".format(self.tablo_ismi,i,"içecekler") 
            self.sorgu_Calistir(sorgu2) 
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")
     
    def su(self): 
        self.liste.append("su")  
        self.txtsiparis.setText(str(self.liste))   

    def kimiz(self):
        self.liste.append("kimiz") 
        self.txtsiparis.setText(str(self.liste))

    def salgam(self):
        self.liste.append("salgam") 
        self.txtsiparis.setText(str(self.liste)) 

    def sari(self):
        self.liste.append("fanta") 
        self.txtsiparis.setText(str(self.liste)) 

    def siyah(self):
        self.liste.append("kola") 
        self.txtsiparis.setText(str(self.liste))

    def ayran(self):
        self.liste.append("yayik ayran") 
        self.txtsiparis.setText(str(self.liste))

    def cay(self):
        self.liste.append("cay") 
        self.txtsiparis.setText(str(self.liste))

    def meyve_suyu(self):
        self.liste.append("meyve_suyu") 
        self.txtsiparis.setText(str(self.liste))

    def kahve(self):
        self.liste.append("kahve") 
        self.txtsiparis.setText(str(self.liste))

class pencere6(pencere):
    def __init__(self,ad,soyad):
        super().__init__()
        uic.loadUi("pencere6.ui",self) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database']='masa_otuzalti'
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.btn_onceki5.clicked.connect(self.onceki5)
        self.btnsiparis_ver.clicked.connect(self.siparis_ver) 
        self.btnsiparis_sil.clicked.connect(self.siparis_sil)
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.liste=[]
        self.btn_sutlac.clicked.connect(self.sutlac)
        self.btn_gullac.clicked.connect(self.gullac)
        self.btn_kazandibi.clicked.connect(self.kazandibi)
        self.btn_puding.clicked.connect(self.puding)
        self.btn_baklava.clicked.connect(self.baklava)
        self.btn_tulumba.clicked.connect(self.tulumba)
        self.btn_profiterol.clicked.connect(self.profiterol)
        self.btn_cake.clicked.connect(self.cake)
        self.btn_dondurma.clicked.connect(self.dondurma)
        self.btn_cek.clicked.connect(self.cek)
        self.gecis()

    def cek(self):
        self.cek_page=siparis(self.txtad.text(),self.txtsoyad.text())
        self.cek_page.show()

    def siparis_sil(self):
        self.liste.clear() 
        self.txtsiparis.setText("")

    def page6(self):
        self.n6=pencere()     
        self.n6.show() 
        self.close()

    def onceki5(self):
        self.lat5=pencere5(self.txtad.text(),self.txtsoyad.text())
        self.lat5.show()
        self.close()

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()

    def siparis_ver(self):
        for i in self.liste:
            sorgu2="insert into `{}` (`siparis`,`siparis_tipi`) VALUES('{}','{}')".format(self.tablo_ismi,i,"tatlilar") 
            self.sorgu_Calistir(sorgu2) 
            time.sleep(1)
            self.lbl_durum.setText("siparişiniz verildi.")

    def sutlac(self): 
        self.liste.append("sutlac")  
        # for self.a  in self.liste:
        self.txtsiparis.setText(str(self.liste))   


    def gullac(self):
        self.liste.append("gullac") 
        self.txtsiparis.setText(str(self.liste))

    def kazandibi(self):
        self.liste.append("kazandibi") 
        self.txtsiparis.setText(str(self.liste)) 

    def puding(self):
        self.liste.append("puding") 
        self.txtsiparis.setText(str(self.liste)) 

    def baklava(self):
        self.liste.append("baklava") 
        self.txtsiparis.setText(str(self.liste))

    def tulumba(self):
        self.liste.append("tulumba") 
        self.txtsiparis.setText(str(self.liste))

    def profiterol(self):
        self.liste.append("profiterol") 
        self.txtsiparis.setText(str(self.liste))

    def cake(self):
        self.liste.append("cheese cake") 
        self.txtsiparis.setText(str(self.liste))

    def dondurma(self):
        self.liste.append("dondurma") 
        self.txtsiparis.setText(str(self.liste))

class siparis(pencere):
    def __init__(self,ad,soyad):
        super().__init__()
        uic.loadUi("siparis.ui",self) 
        self.ad=ad
        self.soyad=soyad
        self.tablo_ismi=self.ad+"_"+self.soyad
        self.txtad.setText(self.ad)
        self.txtsoyad.setText(self.soyad) 
        self.config={'user':'root','password':'','host':'127.0.0.1'}
        self.config['database']='masa_otuzalti'
        self.deneme() 
        self.siparisGoruntule()
        self.btn_siparis_iptal.clicked.connect(self.siparis_iptal)

    def siparisCek(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        a=cursor.fetchall()
        return a

    def sorgu_Calistir(self,sorgu):
        connection=MySQLConnection(**self.config)
        cursor=connection.cursor(dictionary=True)
        cursor.execute(sorgu)  
        connection.commit()
        connection.close()

    def deneme(self):
        try:    
            sorgu1="create table {} (siparis VARCHAR(50), siparis_tipi VARCHAR(50))".format(self.tablo_ismi)
            self.sorgu_Calistir(sorgu1)
        except:
            pass
    
    def siparisGoruntule(self):
        sorgu="select siparis from {}".format(self.tablo_ismi)
        siparis=self.siparisCek(sorgu)
        liste=[]
        for i in siparis:
            liste.append(i['siparis']) 
            self.txt_cek.setText(str(liste)) 

    def siparis_iptal(self):
        self.txt_cek.setText((""))       
        siparis_sil = "delete from {}".format(self.tablo_ismi)
        self.sorgu_Calistir(siparis_sil) 
         



app=QApplication(sys.argv)
q=pencere()
q.show()
sys.exit(app.exec())
