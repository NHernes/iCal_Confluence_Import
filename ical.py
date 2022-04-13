import csv
import csv_ical
from csv_ical import Convert
import pandas
import datetime
from datetime import datetime
from datetime import datetime, timedelta


import csv

f = open('Ausgangsdatei.txt', 'r',  encoding='iso-8859-1')

data = f.read()

splat = data.split("\n")



with open ('Anmeldungen_test.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=';')
    line_count=0
    for row in csv_reader:
                #Nummer=row['Nummer']
                Prüfungsname=row['Prüfungsname']
                LVNummer=row['LV']
                Fachbereich=row['FB']
                Anzahl_Studierende=row['Studierende']
                Prüfungsdauer=row['Dauer']
                DistanzOPräsenz=row['Format']
                Datum_HK=row['Datum_HK']
                Uhrzeit_HK=row['Zeit_HK']
                Datum_NK=row['Datum_NK']
                Uhrzeit_NK=row['Zeit_NK']
                Lehrende=row['Namen']
                Mail=row['Mail']
                Erfahrung=row['Erfahrung']

                Uhrzeit_HK=Uhrzeit_HK.replace("Uhr","")
                #print(Uhrzeit_HK)
                Prüfungsdauer=Prüfungsdauer.replace(" Minuten","")
                if Prüfungsdauer =="andere Prüfungsdauer (bitte am Ende des Formulars im Kommentarfeld angeben)":
                    Prüfungsdauer = "120"
                
                df = pandas.DataFrame({'duration':[Prüfungsdauer]})
                test2=(pandas.to_datetime(df.duration, unit='m').dt.strftime('%H:%M'))



                list5=test2.values.tolist()
                list6=[Uhrzeit_HK]
                liste7=list6+list5

                
                mysum = timedelta()
                for i in liste7:
                   (h, m) = i.split(':')
                   d = timedelta(hours=int(h), minutes=int(m))
                   mysum += d
                mysum=str(mysum)


                mysum=Datum_HK+ " " + mysum
                mysum = mysum.replace(":","")
                mysum =datetime.strptime(mysum, '%d.%m.%Y %H%M%S')
                mysum=mysum.strftime("%Y%m%d %H:%M:%S")
                mysum = mysum.replace("-","")
                mysum = mysum.replace(":","")
                mysum = mysum[:8] + 'T' + mysum[9:]
                print(mysum)




                test=Datum_HK+ " " + Uhrzeit_HK
                test = test.replace("Uhr","")
                test = test[:-1]

                test = datetime.strptime(test, '%d.%m.%Y %H:%M')

                test=test.strftime("%Y%m%d %H:%M")
                test = test.replace("-","")
                test = test.replace(":","")
                test = test[:8] + 'T' + test[9:] +"00"




                liste2=["BEGIN:VEVENT",
                "DTSTAMP:20220411T101111Z",
                "DTSTART;TZID=Europe/Berlin:"""+test+"",
                "DTEND;TZID=Europe/Berlin:"""+mysum+"",
                "SUMMARY:"""+Prüfungsname+ """ HK""",
                "X-CONFLUENCE-CUSTOM-TYPE-ID:ff8ff9e4-9166-464f-96f7-005e76702ec7",
                "CATEGORIES:07.Prüfung fertig erstellt + TN Liste vorhanden",
                "SUBCALENDAR-ID:c36f3bc6-eadb-478b-a457-290cfd40224c",
                "PARENT-CALENDAR-ID:79d9fb7a-dd07-49fc-8e27-c1d40c04e0f8",
                "PARENT-CALENDAR-NAME:",
                "SUBSCRIPTION-ID:",
                "SUBCALENDAR-TZ-ID:Europe/Berlin",
                "SUBCALENDAR-NAME:",
                "EVENT-ID:",
                "EVENT-ALLDAY:false",
                "CUSTOM-EVENTTYPE-ID:ff8ff9e4-9166-464f-96f7-005e76702ec7",
                "DESCRIPTION:"+Lehrende+"",
                "CREATED:20201109T103327Z",
                "LAST-MODIFIED:20201109T103327Z",
                "SEQUENCE:1",
                "X-CONFLUENCE-SUBCALENDAR-TYPE:custom",
                "TRANSP:TRANSPARENT",
                "STATUS:CONFIRMED",
                "END:VEVENT"]

                splat = splat + liste2 



######

                Uhrzeit_NK=Uhrzeit_NK.replace("Uhr","")
                #print(Uhrzeit_HK)
                Prüfungsdauer=Prüfungsdauer.replace(" Minuten","")
                if Prüfungsdauer =="andere Prüfungsdauer (bitte am Ende des Formulars im Kommentarfeld angeben)":
                    Prüfungsdauer = "120"
                
                df = pandas.DataFrame({'duration':[Prüfungsdauer]})
                test2=(pandas.to_datetime(df.duration, unit='m').dt.strftime('%H:%M'))



                list5=test2.values.tolist()
                list6=[Uhrzeit_HK]
                liste7=list6+list5

                
                mysum = timedelta()
                for i in liste7:
                   (h, m) = i.split(':')
                   d = timedelta(hours=int(h), minutes=int(m))
                   mysum += d
                mysum=str(mysum)


                mysum=Datum_NK+ " " + mysum
                mysum = mysum.replace(":","")
                mysum =datetime.strptime(mysum, '%d.%m.%Y %H%M%S')
                mysum=mysum.strftime("%Y%m%d %H:%M:%S")
                mysum = mysum.replace("-","")
                mysum = mysum.replace(":","")
                mysum = mysum[:8] + 'T' + mysum[9:]
                print(mysum)




                test=Datum_NK+ " " + Uhrzeit_NK
                test = test.replace("Uhr","")
                test = test[:-1]

                test = datetime.strptime(test, '%d.%m.%Y %H:%M')

                test=test.strftime("%Y%m%d %H:%M")
                test = test.replace("-","")
                test = test.replace(":","")
                test = test[:8] + 'T' + test[9:] +"00"




                liste15=["BEGIN:VEVENT",
                "DTSTAMP:20220411T101111Z",
                "DTSTART;TZID=Europe/Berlin:"""+test+"",
                "DTEND;TZID=Europe/Berlin:"""+mysum+"",
                "SUMMARY:"""+Prüfungsname+ """ NK""",
                "X-CONFLUENCE-CUSTOM-TYPE-ID:ff8ff9e4-9166-464f-96f7-005e76702ec7",
                "CATEGORIES:07.Prüfung fertig erstellt + TN Liste vorhanden",
                "SUBCALENDAR-ID:c36f3bc6-eadb-478b-a457-290cfd40224c",
                "PARENT-CALENDAR-ID:79d9fb7a-dd07-49fc-8e27-c1d40c04e0f8",
                "PARENT-CALENDAR-NAME:",
                "SUBSCRIPTION-ID:",
                "SUBCALENDAR-TZ-ID:Europe/Berlin",
                "SUBCALENDAR-NAME:",
                "EVENT-ID:",
                "EVENT-ALLDAY:false",
                "CUSTOM-EVENTTYPE-ID:ff8ff9e4-9166-464f-96f7-005e76702ec7",
                "DESCRIPTION:"+Lehrende+"",
                "CREATED:20201109T103327Z",
                "LAST-MODIFIED:20201109T103327Z",
                "SEQUENCE:1",
                "X-CONFLUENCE-SUBCALENDAR-TYPE:custom",
                "TRANSP:TRANSPARENT",
                "STATUS:CONFIRMED",
                "END:VEVENT"]

                splat = splat + liste15 


#####

output_file=open("Output.txt", "w")
splat+=["END:VCALENDAR"]

for i in splat:
    output_file.write(i)
    output_file.write("\n", )
output_file.close()
