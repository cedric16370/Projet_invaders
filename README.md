# Projet_invaders 

But du projet:

Le but de se projet est de réaliser un space invaders en python pour mettre en application se que l'on a appris. Le joueur pourra déplacer son vaisceau à l'aide de l'accélèromètre de la carte STM32, il doit pouvoir tirer à l'aide du bouton poussoir bleu de la carte.

Utilisation: 

1. Activer l'environnement virtuel (venv) à l'aide de la commande: source venv/bin/activate 
2. Flasher la carte à l'aide de la commande: sudo venv/bin/oython pydfu.py --upload
3. Copier coller le code dans main.py qui se trouve sur la clé 
4. Ejecter la clé puis lancer putty sur le bon port COM

Difficultées:

1. Ma première difficultée a été de pouvoir flasher ma carte car j'ai eu un soucis avec mon port USB. Ce qui a rendu compliqué les tests au débuts de mon programme. Le problème a pu être réglé à l'aide de la mise à jour des pilotes.
2. La deuxième a été de réaliser le tire à l'aide du bouton poussoir. Il m'a fallu beaucoup de temps pour réussir plusieurs tire d'affilés, le bouton ne tirait qu'une seule fois. Ce problème a pu être résolu avec l'aide d'un camarade et beaucoup de temps.

Notion apprise:

1. Les classes j'ai appris à réaliser des classes sur pythons afin de pouvoir créer des éléments qui contiennent le skin et la position.
2. Je me suis nettement amélioré sur la création des fonctions et comment les appeller.
3. J'ai découvert comment afficher nos éléments(skin) sur l'uart à l'aide de fonction que l'on a pu créer.

Ce projet aura permis de perfectionné les connaissances en python et à apprendre à les utilisés au bon moment. Tout en s'amusant un réaliser un jeu que tous le monde connait. Les acquis ont pu être renforcé même s'il y eu beaucoup de temps perdu sur des petits détails que l'on ne voit pas forcément directement. On peut conclure que ce projet a été très enrichissant ainsi que très intérresant pour moi car il m'a apporté beaucoup de connaissance.
