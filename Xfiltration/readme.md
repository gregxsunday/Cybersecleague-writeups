# **Xfiltration**

W siedzibie Adui Industries zlokalizowany jest router – znajduje się w supertajnej, ściśle odseparowanej sieci, a whistleblower zdołał się do tej sieci przedostać. W niej zakodowane są interesujące dane. Konieczna jest jednak „eksfiltracja” danych z tej odseparowanej sieci. Router powinniście odnaleźć w czasie poprzednich wizyt w AI. Teraz należy rozpoznać w jaki sposób pozyskać dane, a następnie odczytać je i zaraportować na adres headquarters@cybersecleague.pl
Info o whistleblowera: nadawanie pliku poprzedziłem 3-sekundowym zaświeceniem diody, a po każdym bajcie informacji wstawiłem jeden bit=1 dla synchronizacji

Powyższe zadanie okazało się polegać na odczytaniu transmisji szeregowej emitowanej za pomocą diody na routerze.

Link do oryginalnego video: https://drive.google.com/file/d/1g2RuYJ4CpHJp_axKoD9uYE_XLTiCHiRA/view

1.```python blinks2bits.py``` zrzuca mignięcia z video do pliku led.txt.

2.```python read_blinks.py``` zamienia mignięcia na bity i zapisuje do pliku bits.txt. Odczyt z wideo nie jest jednak w 100% dokładny.

3.```python manual_finalization.py``` wczytuje bity z pliku bits.txt i wypisuje je w takiej formie, żeby dało się wychwycić miejsca, w których bit synchronizacyjny nie jest równy jeden. Od tego punktu trzeba ręcznie dopisywać lub usuwać bity tak, aby otrzymać znaki drukowalne.
