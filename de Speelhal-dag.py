persoon = 3 #euro
toegangsticket = 7.45 #euro
VIPVRtijd = 45 #minuten
VIPVRKoste = 0.37 #euro, het kost 0.37 per 5 minuten


print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar" + (str( persoon * toegangsticket + VIPVRtijd / 5 * VIPVRKoste) + " euro."))