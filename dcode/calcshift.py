import pandas as pd
import statistics
# siehe auch https://docs.python.org/3/library/statistics.html

# einfache Verschiebungsberechnung durch Ermittelung des Median 
# übergeben werden das dataframe mit den DCodes und der DCode für den gerechnet werden soll
# zurück gegeben werden der ´Mittelwert und die Anzahl der Treffer
# zur weiteren auswertung kann auch die Trefferliste zurück gegeben werden
# und später auch ein getrimmter Suchstring

def calcshift(dataframe,suchstring,dbid=0):
    calcshift=-999
    #print(suchstring)
    #wert3 = dataframe[dataframe['DCode'].str.contains(suchstring)]['Shift']
    # Es kann dbid übergeben werden, wenn Tests mit Daten aus der NMRShiftDB gemacht werden
    '''
    wert3 = dataframe[
         (dataframe['DCode'].str.contains(suchstring)) & 
         (dataframe['Database_ID'] != dbid)
    ]['Shift']    
    treffer= len(wert3)
    '''
    # rekursion zur String Kürzung
    # Initiale Bedingungen
    treffer = 0  # Setzen Sie treffer initial auf 0, um die Schleife zu starten
    min_hashes = 5  # Minimale Anzahl an '#' im Suchstring
    kuerz=0
    # Solange die Bedingungen erfüllt sind
    while treffer == 0 and suchstring.count('#') >= min_hashes:
        # Kürzen des Suchstrings bis zum letzten '#' 
        last_hash_index = suchstring.rfind('#')  # Finde den Index des letzten '#'
    
        if last_hash_index != -1:  # Überprüfen, ob ein '#' gefunden wurde
            suchstring = suchstring[:last_hash_index]  # Kürzen bis zum letzten '#'
        
            # Erneute Berechnung von wert3 und treffer
            wert3 = dataframe[
                 (dataframe['DCode'].str.contains(suchstring)) & 
                 (dataframe['Database_ID'] != dbid)
            ]['Shift']
        
            treffer = len(wert3)  # Aktualisieren der Trefferzahl
            kuerz+=1
        else:
             break  # Schleife beenden, wenn kein '#' mehr gefunden wird
    
    ## Ende der rekursion
    if (treffer > 0):
        median_wert = statistics.median(wert3)        # median als chemische Verschiebung
    else:
        median_wert = -999
    calcshift = median_wert
    return calcshift, treffer, kuerz