import requests # Envoyer des requêtes HTTP
from lxml import html
from bs4 import BeautifulSoup # Consulter et de manipuler la structure arborescente d’un document HTML.
import json
from os import path
import matplotlib.pyplot as plt
import smtplib, ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import PhotoImage
import time

filename = 'produits.json'


# while(True):    ----> Tant que c'est vrai
#    time.sleep(x) ----> se lance toutes les Xs
window = Tk()
    # Creer la frame ( boite )
frame = Frame(window, background='#131921')
    # personnaliser fenetre
window.title("Mon application")
window.geometry("2040x720")
window.minsize(700, 500)
window.config(background='#131921')
# Ajout de l'image
logo = PhotoImage(file="logoamazon.png")
logo = logo.subsample(2, 2)
label_logo = Label(frame, image=logo, background='#131921')
label_logo.pack(pady=50)
# premier texte
label_title = Label(frame, text="Entrez l'URL Amazon", font=('Courrier', 25), fg='white', background='#131921')
label_title.pack()




def get_prix(url):
    headers = {
            'User-Agent': 
            'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept-Encoding': None
        }
    url = entry_url.get()
    reponse = requests.get(url, headers=headers) # On envoie une requête vers l'url, on la met ensuite dans une variable réponse
    tree = html.fromstring(reponse.content) # Prendre contenu de html
    # Regler probleme index out of range
    prix_list = tree.xpath('//span[@class="a-offscreen"]/text()')
    if len(prix_list) > 0:
        prix = prix_list[0]
        prix, signe = prix.split("€",1) # Enlever signe euro avec split
    produit_list = tree.xpath('//span[@id="productTitle"]/text()')
    # Regler probleme index out of range
    if len(produit_list) > 0:
        produit = produit_list[0]
    date = reponse.headers['Date'] # Date heure a laquelle le script est lancé
    nouveau = {'Produit': produit_list, 'prix': prix_list, 'date': date}
    return nouveau



def get_json():
        # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")
        #list = []
    historique = []
    with open(filename, 'r') as outfile:
        if path.getsize(filename) != 0:
            historique = json.load(outfile)
    return historique



def update_data(historique, nouveau):
    historique.append(nouveau)
    return historique



def update_json(entry_url):
    url = entry_url.get()
    print(url)
    nouveau = get_prix(entry_url)
    historique = get_json()
    new_list = update_data(historique, nouveau)
    with open(filename, 'w') as outfile:
        json.dump(new_list, outfile, indent=4)



    # zone de saisie
entry_url = Entry(frame, font=('Courrier', 20), background='#ffffff')
entry_url.pack()
    #ajouter bouton

button = Button(frame, text='Validez', background='#131921', font=('Courrier', 20), fg='white', command=lambda: update_json(entry_url))
button.pack(pady=25, fill=X)
    #button.pack(update_json(entry_url.get()))
    # afficher le frame
frame.pack(expand=YES)

window.mainloop()


#----------------------------------------------------ENVOI DU MAIL--------------------------------------------------

"""

ANCIEN CODE A SEPARER DU NOUVEAU

#-------------------------------------------------------------------------------------------------------------
window = Tk()
# Creer la frame ( boite )
frame = Frame(window, background='#70c36d')
# personnaliser fenetre
window.title("Mon application")
window.geometry("2040x720")
window.minsize(480, 360)
window.config(background='#70c36d')
# premier texte
label_title = Label(frame, text="Entrez l'URL Amazon", font=('Courrier', 25) ,background='#70c36d')
label_title.pack()

def prix_titre():
        # user agent, headers du protocole http 
        # ( paramètres envoyé par navigateur lorsqu'il dmd une page web ) 
        # permet de fr croire au site qu'on utilise un navigateur normal et pas python
    headers = {
                'User-Agent': 
                'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept-Encoding': None
        }
    url = entry_url.get()
    reponse = requests.get(url, headers=headers) # On envoie une requête vers l'url, on la met ensuite dans une variable réponse
    tree = html.fromstring(reponse.content) # Prendre contenu de html
    prix = tree.xpath('//span[@class="a-offscreen"]/text()')[0] # 0 pour prendre premier produit sinon affiche tous prix de la page
    prix, signe = prix.split("€",1) # Enlever signe euro avec split
    prix = prix.replace(',', '.') # remplacer virgule par point
    title = tree.xpath('//span[@id="productTitle"]/text()')[0] # 0 ici pour enlever les crochets
    date = reponse.headers['Date'] # Date heure a laquelle le script est lancé
        #print(reponse.headers)
        #print(title, prix)


#-----------------------------------------------PLUSIEURS DONNEES DANS JSON------------------------------------------


    filename = 'produits.json'
        # Check if file exists
    if path.isfile(filename) is False:
            raise Exception("File not found")
        #list = []
    data = {'Produit': title, 'prix': prix, 'date': date}
    json_data = []
    with open(filename, 'r') as outfile:
        if path.getsize(filename) != 0:
                json_data = json.load(outfile)
                #print(type(json_data))
                #print("data from file: " + str(json_data))
                json_data.append(data)
        else:
            json_data = [data]
                #print("data first time : " + str(json_data))

    with open(filename, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

    product_data = []
    for i in json_data:
        if i['Produit'] == title:
            product_data.append(i)

    if str(prix) > str(product_data[-2]['prix']) :
        print('Prix du baissé, mail envoyé')
        evolution_prix = "Le prix du :\n" + title + "\na baissé, un mail vous a été envoyé"
        mail_envoi(url)
    else: 
        print('Prix du pc non baissé, mail non envoyé')  
        evolution_prix = "Le prix du :\n" + title + "\nn'a pas baissé : " + prix + " €" + " \nDésolé!"
            

    frame.destroy()
    frame2 = Frame(window, background='#70c36d')
    label2_title = Label(frame2, text="L'URL a bien été validé", font=('Courrier', 25), background='#70c36d')
    label2_title.pack()
    label3_title = Label(frame2, text=evolution_prix, font=('Courrier', 15) ,background='#70c36d')
    label3_title.pack()
    frame2.pack(expand=YES)


#-------------------------------------------------------------------------------------------------


# zone de saisie
entry_url = Entry(frame, font=('Courrier', 20), background='#ffffff')
entry_url.pack()
#ajouter bouton
button = Button(frame, text='Validez', background='#70c36d', font=('Courrier', 20), fg='white', command=prix_titre)
button.pack(pady=25, fill=X)
# afficher le frame
frame.pack(expand=YES)
# afficher fenetre
window.mainloop()

 
#----------------------------------------------------GRAPHIQUE------------------------------------------------------

data = pd.read_json('produits.json') # Lire le fichier dans lequel on veut les infos
#data = json_data
plt.title("Graphique produit Amazon") # titre du graphique
plt.plot(data['date'], data['prix'].apply(lambda x: float(x)), "r+") #Date = données pour abcisse(bas), Prix = Données pour ordonnées(côté) # "g--", linewidth=1 // Pour tracer en ligne
plt.xlabel("Date/Heure") # Données légende a l'abcisse
plt.ylabel("Prix") # Données sous-titre aux ordonnées
plt.show() # Montrer le graphique


def mail_envoi(url, produit_data):
    email_sender = 'testsendmail617@gmail.com'
    email_password = 'mdpdappli'
    email_receiver = 'ojgoigjdofijg@gmail.com'

    subject = 'Suivi de votre produit Amazon'    
    produit = produit_data['produit'] 
    prix = produit_data['prix']
    body = "Le prix du " + produit + " est en baisse à " + prix + "€, vérifiez avec le lien : " + url
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
"""




"""
def automatisation():
    cron_command = "25  6   *  1   *  python3 -c 'import scraptest.py: scraptest.py.compare(\'url\')"
    set_cron(scraptest.py)
"""


