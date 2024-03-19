NB: la commande "git clone --bare url_repo_existant" duplique un référentiel git existant 
mais sans tous les tags et sans toutes les reférences (sur d'éventuelles branches partagées)

Via l'option complémentaire(ou alternative et sous entendue complémentaire)  --mirror , la commande "git clone --mirror url_repo_existant"
duplique plus en profondeur un référentiel git existant de manière à ce que la duplication soit fonctionnelement identique à l'original.
Il y a en plus une duplication DYNAMIQUE/ACTUALISABLE des tags et des références sur d'éventuelles branches à pister .

NB: après une duplication via "git clone --mirror ..." , au niveau du clone distant créé (de type "xyz.git") 
on pourra récupérer/réactualiser des copies des références sur les branches distantes via "git remote update" ou bien "git fetch --all"

Concrètement(autrement dit), un clone (dévéloppeur/ordinaire) d'un "bare_mirror" pourra voir des branches envoyées sur le référentiel_git_bare_original
après un "git fetch --all" sucessivement déclenché à 2 niveaux (d'abord sur le "bare_mirror" , ensuite sur le clone_developpeur issu du mirroir). 

