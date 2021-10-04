# tp-dockerfile
- Créez une image docker "factiorielle" qui permets de renvoyer le factorielle d'un nombre n en entrée en lançant le script app_1.py, vous devez :
    - Définir votre repertoire de travail "factorielle"
	- Copier votre repertoire de travail dans le repertoire défini
	- Exposer le port 80
	- Lancer le script exo1/app_1.py au démarrage du conteneur avec "number" comme un parametre input ( python exo1/app_1.py --number 5 )
	- Lancez votre conteneur en 2 méthodes ( interactive, detachée ) 
		
- Créez une image docker "hello-flask" qui permet d'afficher la valeur de la variable d'environnement NOM en lançant le script app_2.py, vous devez:
	- Définir votre repertoire de travail "app"
	- Copier votre repertoire de travai dans le répertoire défini
	- Installer les dépendances necessaire ( installer le requirements.txt ) pour lancer le script app_2.py 
	- Déclarer votre variable d'environnement NOM qui prendra comme valeur votre prénom
	- Exposer le port 9999
	- Lancer le script exo2/app_2.py au démarrage du conteneur
		
- Créez une image docker "list-directory" qui permet de lister le contenu de votre repertoire courant en 2 méthodes :
	- En lançant le script exo3/app_3.py au démarrage du conteneur
	- Dans un 1er temps mettre à jour les independances, ensuite executer la commande "ls" au démarrage du conteneur
	- Pour les 2 méthodes, vous devez embarquer seulement le répertoire exo3 (2 manières possibles), votre commande devra afficher le contenu du repertoire tp-dockerfile
