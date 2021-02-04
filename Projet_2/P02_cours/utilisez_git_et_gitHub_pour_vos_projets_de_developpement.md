### 1) Tirez le maximum de ce cours !
* Contenu du cours
    * Le contrôle de versions
    * Les dépôts
    * Les commandes Git
    * Réparé ces erreurs
***
### 2) Découvrez la magie du contrôle de versions
* La différence entre Git et Github
    * Git est un outil (un gestionnaire de code source) qui sauvegarde l'historique des versions du codes en créant un dépôt local
    * Github stock le code
####
* Git travail en local ce qui signifie sur votre machine, par opposition à "en ligne"
####
* L’intérêt de ce type d'outil est donc de pouvoir revenir sur n’importe quelle version en cas de bug dans l’application
####
* Git est souvent utilisé dans l'open source
    * Open source signifie que le code source d'un logiciel est public et accessible. Le logiciel peut alors être modifié et diffusé par n'importe qui
####
* La maîtrise de Git est très souvent demandée lors d’un recrutement, c’est pourquoi il est essentiel de le maîtriser
***
### 3) Saisissez l'utilité des dépôts distants sur GitHub
*  Avantages d'un dépôt
   * Stockage du code
   * Contrôle de versions
   * Sauvegarde des changements
   * Code sécurisé
####
* Il y a deux types de dépôts
   * Dépôt privé (seul les personnes autorisées ont accès) 
   * Dépôt public (visible de tous et des personnes peuvent y collaborer)
####
* Github est comme une bibliothèque numérique qui contient tous les codes écris
####
* GitHub, est devenu depuis quelques années le book/portfolio des développeurs
***
### 4) Démarrez votre projet avec GitHub
* GitHub est un service en ligne permettant d’héberger ses dépôts distants
####
* Il faut s'inscrire pour créer des dépôt sur Github 
####
* Pour créer un dépôt sur github (un repository), Cliquez sur le "+" dans le coin supérieur droit, pour faire apparaître l’option New repository
####
* Lui donner un nom
####
* Choisir Si le dépôt sera public ou privés (il sera public en général)
####
* Puis cliquez sur "Create repository"
***
### 5) Installez Git sur votre ordinateur (initialisation d'un 1er projet)
* Rendez-vous sur le site https://git-scm.com/downloads
####
* Sélectionner votre OS et suivez les instructions   
####
* Initialisez Git (configuration de base au départ, avec l'option --global, vous n’aurez besoin de le faire qu'une fois)       
  `git config --global user.name "votre nom`  
  `git config --global user.email votre_adresse_mail@example.com`  
  `git config --global color.ui true`
####
* Il est possible de vérifier la configuration de git par la commande suivante    
`git config --list`
####
* Création d'un dépôt local (sur votre machine)
  * Créer un dossier sur votre pc
  * Rendez-vous dans votre dossier
  * Tapez la commande suivante pour initialiser comme nouveau projet dans ce dossier  
  `git init`
  * Un dossier caché .git a été créé (dossier caché)
***
### 6) Utilisez les commandes de base de Git !
* Récupérer et cloner un dépôt distant
  * Récupérer l'url du dépôt distant
  * Se rendre dans votre dossier initialisé par la commande `git init`
  * Taper la commande suivante  
  `git remote add nom_du_depot_distant_de_votre_choix url_précédemment_récupérée`
> nom_du_depot_distant_de_votre_choix" représente le nom court pour appeler votre dépôt. Un nom court et simple est toujours plus facile 
####
* Maintenant que notre dépôt local pointe sur le dépôt distant, nous allons cloner son contenu   
`git clone url_précédemment_récupérée`
####
* Le principal atout de Git est son système de branches
  * Les différentes branches correspondent à des copies de votre code principal à un instant T  
  * la branche principale est appelée la branche "main" 
####
* Pour connaître les branches présentes dans notre projet
  * taper la commande "git branch"
    * Cela affichera vos branches et indiquera une "*" devant la banche active à ce moment la
      * S'il n'y a aucune branche en tapant cette commande cela veut dire qu'il n'y a pas encore eu de 1er commit
####
* Pour créer une branche  
`git branch nom_de_la_branche`  
####
* Pour supprimer une branche  
`git branch -d nom_de_la_branche`
    * Il y a aussi la commande  
      `git branch -D nom_de_la_branche` (le "-D" est en majuscule)
      * Cela entraînera la suppression de tous les fichiers et modifications que nous n'aurez pas commités sur cette branche
####
* Pour vous rendre sur une branche  
`git checkout nom_de_la_branche`
####
* Pour vous renommer une branche il faut se positionner dessus  
`git branch -M nouveau_nom_de_la_branche`
####
* Git gère les versions des travaux locaux à travers 3 zones locales majeures
  * La 1ére étape est "untracked" (l'état avant modification)
  * La 2éme étape est "staging" (enregistrement des modifications)
  * La 3éme étape est "commit" (sauvegarde des modifications)
####
* Réaliser un "staging"
  * Un staging est tout simplement un enregistrement de votre travail sur la branche courante  
`git add nom_du_fichier`
> Il y a aussi la commande `git add --all` pour tout enregistrer d'un coup
####
* Réaliser un "commit"
  * Un commit est tout simplement un sauvegarde de votre travail à un instant T sur la branche courante  
`git commit -m "indiquer ce que vous venez de modifier" nom_du_fichier_a_commit`
> Le "-m puis les guillemets" pour indiquer le message du commit
####
* La commande "Git push" permet d'envoyer les modifications que l'on a réalisées en local sur le dépôt à distance  
`git push -u nom_du_depo_distant nom_de_la_branche_a_envoyer`
***
### 7) Corrigez vos erreurs sur votre dépôt local
* Tant que le commit n'a pas encore été fait on peut utilisé une remise avec "git stash"  
`git stash` (mets le staging dans une zone tampon)  
  * Créer la nouvelle branche  
`git stash list` pour vérifier les "stash" en attente  
`git stash apply nom_du_stash`
  * Il reste plus qu'à commit le fichier sur la nouvelle branche
####
* Analyser les commits  
`git log`
  * `git log --one-line` (affiche les commits sur une seule ligne)
####
* Supprimer le dernier commit  
`git reset --hard HEAD^`
> Cette commande supprimera votre dernier commit. Le Head^ indique que c'est bien le dernier commit qui sera supprimer.  
####
* Modifier le message du commit précédent sans modifier son instantané  
`git commit --amend -m "Votre nouveau message de commit`
####
* Rajouter un fichier au dernier commit  
`git add FichierOublie.txt`  
`git commit --amend --no-edit`
***
### 8) Corrigez vos erreurs sur votre dépôt distant
* Si vous avez un push si le dépôt distant la première chose à faire est de prévenir les collaborateurs du projet.
####
* Pour annuler ce dernier commit  
`git commut revert HEAD^`  
> Gardez à l'esprit que Git revert sert à annuler des changements commités, tandis que Git reset HEAD permet d'annuler des changements non commités   
>
> Toutefois, attention, Git revert peut écraser vos fichiers dans votre répertoire de travail, il vous sera donc demandé de commiter vos modifications ou de les remiser
####
* Connection au dépôt distant avec une clé SSH  
  * Générer une clé SSH  
`ssh-keygen -t rsa -b 4096 -C "johndoe@example.com"`  
> Vous pouvez soit appuyer sur Entrée, soit indiquer un nom de fichier. Un mot de passe vous est ensuite demandé   
>
> La clé id_rsa.txt est votre clé privée alors que la clé id_rsa.pub est votre clé publique
####
* Ajout de la clé au dépôt Github
  * Connectez-vous à votre espace GitHub puis allez dans l'angle droit de votre compte et cliquez sur Settings
  * Cliquez sur SSH and GPG keys
  * Puis sur New SSH Key 
  * Choisissez un titre et collez votre clé SSH
  * Vous devrez ensuite confirmer votre mot de passe, et votre clé SSH sera alors ajoutée à votre compte GitHub
***
### 9) Utilisez Git reset
* Il y a 3 types de commandes avec Git reset 
  * Sotf  : Ne supprime aucun fichier (revient au staged avant le commit) 
  * Mixed : Reviens jusqu'au dernier commit (aucune suppression faites)
  * Hard  : modification qui ne peuvent être annuler et commit supprimer pour toujours
> Attention, si vous exécuter cette commande "Hard", vérifiez 5 fois avant de la lancer et soyez sûr de vous à 200 %
* Git resert --hard  
`git reset notreCommitCible  --hard`  
> Cette commande va permettre de revenir à n'importe quel commit mais en oubliant absolument tout ce qu'il s'est passé après !    
> Quand je dis tout, c'est TOUT ! Que vous ayez fait des modifications après ou d'autres commits, tout sera effacé ! C'est pourquoi il est extrêmement important de revérifier plusieurs fois avant de la lancer, vous pourriez perdre toutes vos modifications si elle est mal faite
####
* Git resert --mixed (Si rien n'est spécifié après  git reset, par défaut il exécutera)  
`git reset --mixed HEAD~`
> Cette commande va permettre de revenir juste après votre dernier commit ou le commit spécifié, sans supprimer vos modifications en cours.   
>
> Il va par contre créer un HEAD détaché. Il permet aussi, dans le cas de fichiers indexés mais pas encore commités, de désindexer les fichiers
####
* Git resert --soft
> Le git reset --Soft permet juste de se placer sur un commit spécifique afin de voir le code à un instant donné ou créer une branche partant d'un ancien commit.    
>
> Il ne supprime aucun fichier, aucun commit, et ne crée pas de HEAD détaché 
####
***Le HEAD, si vous n'êtes pas sûr d'avoir bien compris, est un pointeur, une référence sur notre position actuelle dans notre répertoire de travail Git. Par défaut, HEAD pointe sur la branche courante, master, et peut être déplacé vers une autre branche ou un autre commit.***
####
* En cas de conflits, ouvrer le fichier avec "vim" ou un autre éditeur
  * Régler le conflit et faire un commit pour valider le changement
####
* Pour annuler la dernière modification (en créant un commit d'annulation)  
`git revert HEAD^`
***
### 10) Corrigez un commit raté
* Consulter l'historique de votre projet (énumère en ordre chronologique inversé)    
`git log` ou `git reflog` 
####
* La commande  git blame  permet d’examiner le contenu d’un fichier ligne par ligne et de déterminer la date à laquelle chaque ligne a été modifiée, et le nom de l’auteur des modifications  
`git blame monFichier.txt`
####
* Cherry-pick sert à dupliquer un commit
  * Se rendre sur la branche du commit à dupliquer faire un `git log` pour récupérer le SHA
  * Retourner sur la branche sur laquelle on veut dupliquer le commit et exécuter la commande     
`git cherry-pick SHA_du_commit`
***
### 11) Identifiez la structure de fichier de Git
* La structure du fichier git
  * Il y a 3 objets dans la structure
    * Le commit (va pointer vers un arbre spécifique et le marquer, pour représenter son état à un instant donné, le plus récent s'appelle "HEAD")
    * Le tree (une forme de répertoire. Il va référencer une liste de trees et de blobs "sous-répertoires et fichiers")
    * Le blob (représente en général un fichier "Binary Large Object")
> Git n'utilise donc pas les noms des fichiers et des répertoires pour classer et stocker vos données, mais il utilise leur empreinte ou identifiant SHA-1 
* Représentation d'un commit
  * Chaque commit a son empreinte unique (le hash SHA-1)  
* Les 3 commandes pour metre à jour le dépôt local 
  * git fetch : extrait les commits les plus récents du dépôt distant et les clonent sur le dépôt local  
  * git merge : relie ce qui est importé par git fetch 
  * git pull  : c'est l'équivalent de faire un git fetch + git merge (si on est sûr que cela va pas créer de conflit)  
> Git fetch, contrairement à Git pull, va aller chercher les modifications sur le dépôt distant mais ne va pas les fusionner avec nos modifications locales  
> Si vous souhaitez fusionner ces données pour que votre branche soit à jour, vous devez utiliser ensuite la commande Git merge
>
> Si les deux branches que vous essayez de fusionner modifient toutes les deux la même partie du même fichier, Git ne peut pas déterminer la version à utiliser. Lorsqu'une telle situation se produit, Git s'arrête avant le commit de merge, afin que vous puissiez résoudre manuellement les conflits 
> 
> La commande  git pull  exécute d'abord  git fetch  qui télécharge le contenu du référentiel distant spécifié. Ensuite, un git merge  est exécuté pour fusionner les modifications du dépôt distant et créer un nouveau commit de merge en local   
>
>***Le choix de la commande à utiliser dépend de la façon dont vous souhaitez travailler***   
***
### 12) Modifiez vos branches avec Rebase
* Git rebase   
`git rebase nom_de_la_branche`
> Git rebase a le même objectif que Git merge. Ces deux commandes permettent de transférer les changements d'une branche à une autre 
>
> Il existe deux types de rebase : le rebase manuel et le rebase interactif  
> Le rebase permet de garder un historique plus clair et plus compréhensible  
> >***Attention ! Vous ne devez jamais rebaser des commits pushés sur le dépôt public ! Cela remplacerait les anciens commits du dépôt public, et cela  serait comme si votre historique avait brusquement disparu*** 
* Git rebase interactif   
`git rebase -i SHA_du_commit` 
> Le rebasage interactif vous donne donc un contrôle complet sur l'historique de votre projet. Il sert principalement à nettoyer son historique. Il est beaucoup apprécié des développeurs qui aiment nettoyer leurs historiques avant de pousser sur le dépôt distant        

* Par exemple, vous avez trois commits ; on va faire simple, ils s’appelleront commit1,  commit2 et commit3. C'était difficile, comme noms ! :pImaginons que vous deviez mettre le commit2 avant le commit1 et que vous vouliez supprimer le commit3. On va faire un rebase interactif sur nos trois derniers commits       
`git rebase -i HEAD~3`   
####
* Puis vous utiliserez la commande Pick pour indiquer à Git dans quel ordre vous les voulez, et la commande Drop pour la suppression du commit3.   
`drop 58gfbg56 commit3`  
`pick 14hg58g1 commit2`  
`pick 25frgf83 commit1`
> N'oubliez pas que l'on appelle toujours les commits par leurs SHA-1  
> Le premier "pick" dans "vim" est le 1er dans le `git log` en partant du bas

* Autre exemple, la commande Git rebase interactif permet aussi de modifier les messages de commit. Imaginons que nous voulions agir sur le dernier commit   
`git rebase -i HEAD^`
####
* Pour modifier ensuite son message de validation, nous allons utiliser la commande Edit        
`edit 54dfiosd`    
####
* Ensuite vous devrez alors faire  
`git commit --amend`
####
* Puis modifier votre message de commit et enfin valider en faisant  
`git rebase --continue`
***
### 13) Utilisez des techniques de nettoyage de branche
* Il est important de toujours nettoyer son historique avant d'envoyer sur le dépôt à distance !
####
* Sélectionnons les deux derniers commits  
`git rebase -i HEAD~2`  
####
* Puis supprimons-les avec la commande Drop  
`drop 58gkbg56 commit52`  
`drop 899hbg78 commit53` 
####
* Supprime les branches non suivies   
`git branch -d brancheTest`
####
* Le squash, est un regroupement de plusieurs commits  
`git rebase -i HEAD~3`
####
* On leur applique la commande Squash   
`pick 57dcsd58 Création du formulaire`  
`squash 58gkbg56 Design Formulaire`  
`squash 899hbg78 Correction du formulaire` 
> Concrètement, on dit à GIT de se baser sur le premier commit et on lui applique tous les suivants pour n’en faire qu’un seul.  
> Lorsque l’on valide le squash, Git va réappliquer les commits dans le même ordre dans lequel ils ont été configurés juste avant. 
On met alors un message de commit qui concerne le regroupement de nos commits
* On perd beaucoup de temps à déboguer notre application, git se propose de réduire ce fameux temps de recherche grâce à Git bisect
* Le but est de retrouver le premier commit où le bug est apparu, mais il faut bien entendu avoir réalisé des commits réguliers
* On commence par la commande start  
`git bisect start [bad] [good]`
> Au lieu de bad, vous devrez mettre le hash d'un commit où le bug est présent. À la place de good, vous devrez mettre le hash d'un commit où le bug n'était pas présent  

> Git va se déplacer sur chaque commit et vous allez devoir, pour chacun de ces commits, lui indiquer si le commit est good ou bad.   
* Si le commit ne présente pas le bug  
`git bisect good` 
####
* Si le commit présente le bug  
`git bisect bad` 

> Une fois chaque commit vérifié, Git va vous indiquer le commit qui a provoqué le bug. Il va l'indiquer de cette manière

    fvsd54g5s5d4g5f34g5dfg47df578q9qdff6 is first bad commit
    commit fvsd54g5s5d4g5f34g5dfg47df578q9qdff6
    Author: Moi <Moi@example.com>
    Date: Tue mar 27 16:28:38 2019 -0800
    
    Add fonctionnality AB
> Il ne vous reste plus qu'a trouver dans vos modifications, la modification qui a engendré le problème
***
### 14) Intégrez les dépôts d’autres personnes dans le vôtre
> Les sous-modules reposent sur l'imbrication de dépôts : vous avez des dépôts… dans des dépôts
> 
> Concernant les sous-arborescences, il n'y a pas de dépôts imbriqués : on n'a qu'un dépôt, le conteneur. Les sous-arborescences sont plutôt un concept
* Cette commande va ajouter à notre dépôt courant le projet ProjetSubModule, comme sous-module dans le dossier Dossier/Destination  
`git submodule add https://github.com/etudiantOC/ProjetSubModule dossier/destination` 
> Vous noterez également qu'au travers de cette opération, Git a ajouté un nouveau fichier de configuration nommé .gitmodules contenant la description des sous-modules utilisés par le projet 
* la différence avec les sous-arborescences   
`git subtree push -P monRépertoire git@mon-serveur-git:group/projet.git master`
> Git subtree va vous permettre de créer un nouvel arbre de commits pour un sous-dossier de votre dépôt Git. Autrement dit, Git subtree régénère l’historique d’un dossier
> 
> Votre répertoire va être pushé sur votre nouveau dépôt distant sur la branche master
***
### 15) Travaillez en équipe en utilisant un workflow
* Un workflow Git est une recommandation sur la façon d'utiliser Git pour effectuer un travail de manière cohérente et productive, le plus connu est GitFlow
  * Une branche Master  : corresponds à notre environnement de production
  * Une branche Hotfix  : permets de corriger un bug en production
    * La branche Hotfix ne doit être utilisée que pour de minimes corrections !
  * Une branche Develop : centralise toutes les nouvelles fonctionnalités qui seront livrées dans la prochaine version
  * Une branche Feature : permets de commencer à travailler sur une nouvelle fonctionnalité
  * Une branche Release : créée à partir de la branche Develop en cas de livraison en production imminente
> GitFlow est une méthode, une architecture Git permettant de séparer au maximum le travail et de toucher le moins possible à la branche master.   
>
> Cette méthode représente donc une architecture en branches. GitFlow est une des architectures les plus connues.       
> 
> GitFlow n'ajoute aucun concept ni aucune commande, il attribue plutôt des rôles très spécifiques aux différentes branches et définit comment et quand elles doivent interagir. 
>
> Pour utiliser GitFlow, il va falloir dans un premier temps l'installer. Une fois GitFlow installé, vous pouvez l'utiliser dans votre projet en exécutant la commande et suivre les instructions   

`git flow init` 
***
### 16) Améliorez Git avec des outils supplémentaires
* Quelques outils qui vous faciliteront la vie divisée en 5 catégories initialement
  * Qualité du code
  * Analyse du code
  * Intégration en continue
  * Suivi
  * Gestion de projet
####
*  Voici quelques-uns des outils les plus connus et les plus utilisés de la marketplace de GitHub  
    * Sécurité : WhiteSource Bolt   
      > WhiteSource Bolt for GitHub est une application gratuite, qui analyse en permanence tous vos dépôts, détecte les vulnérabilités des composants open source et apporte des correctifs. Il prend en charge les référentiels privés et publics
    * Gestion de projets : ZenHub
      > ZenHub est le seul outil de gestion de projet qui s'intègre de manière native dans l'interface utilisateur de GitHub. ZenHub est un outil de gestion de projet agile fonctionnant par sprint et générant des rapports assez poussés 
    * l'intégration continue : Travis CI
      > Travis CI permet à votre équipe de tester et déployer vos applications en toute confiance. Très polyvalent, il s'adapte aux petits comme aux grands projets   
    * Le comparateur de code : Les plus connus, WinMerge et Meld
      > En plus de vous indiquer les différences entre vos deux fichiers, vous allez pouvoir les fusionner de façon intelligente. Pour chaque ligne différente, l'outil de comparaison vous demandera quelle version vous souhaitez conserver. Il est donc indispensable en cas de conflit dans Git
 
* ###***Il existe bien sûr de nombreux autres outils sur la marketplace***
***
### 17) Utilisez le GitLab intégration continue (IC)
* Ce qu’il faut retenir sur GitLab :

      - Il permet d’héberger les projets web et la gestion de versions des codes sources
      - Il permet la gestion de tout le processus de développement
      - Il permet une collaboration simple
      - Il est open source et collaboratif
      - C’est gratuit
      - C’est aussi une solution pour les entreprises
####
* GitLab est donc une réelle alternative à GitHub ! En effet, GitLab CI est un système d'intégration continue très puissant et gratuit  
####
* GitLab CI/CD va vous permettre d’automatiser les builds, les tests, les déploiements, etc.  de vos applications. L’ensemble de vos tâches peut être divisé en étapes et l’ensemble de vos tâches et étapes constituent un pipeline
####
* Quels sont les outils de CI
  * Jenkins : l'un des premiers serveurs d'intégration continue open source, et reste l'option la plus couramment utilisée aujourd'hui
    
        - Logiciel gratuit   
        - Plus de 1 000 plugins sont disponibles   
        - Vous pouvez créer un plugin si celui que vous désirez n'existe pas   
        - Vous pouvez également partager ce plugin   
        - Logiciel facile à installer   
    * Nous pouvons évoquer aussi Buildbot, Drone, Concourse, mais Jenkins et GitLab restent les maîtres en la matière   
***
### 18) Gérez les demandes de pull
* Il est très important de gérer les demandes de pull request régulièrement, si vous souhaitez garder une communauté active et avoir un projet vivant   
* Les badges permettent de garder le projet à jour et indiquent une certaine qualité. Les badges peuvent être utilisés pour tout un tas de choses
* Les "issues" permettent aux utilisateurs et aux contributeurs d'indiquer des bugs afin qu'ils puissent être corrigés par vous, mais aussi par les autres contributeurs
####
> Vous vous demandez sûrement comment être sûr de ne pas fusionner n'importe quoi sur votre branche principale
>
> Tout d'abord, vous devez bien entendu regarder ce que l'on vous a transmis
> 
> Ensuite, sur des projets plus conséquents, vous pouvez indiquer un nombre minimum d'approbations (par les autres contributeurs), avant d'avoir la possibilité de fusionner.
> C'est un gage de sécurité et de qualité
***
