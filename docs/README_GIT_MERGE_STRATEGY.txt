git merge -s recursive -X ours YoursBranch
NB: -X ours est une option de la strategie recursive . 
    Cette combinaison permet de garder notre version (à nous locale) en cas de conflit avec d'autres branches
    Les éléments des autres branches qui ne sont pas en conflit sont récupérer lors de cette fustion automatique

NB: il existe aussi "git merge -ours YoursBranch" encore plus radicale (qui ignore tout le contenu des autres branches) 
    et qui ne conserve que ce qu'il y a dans notre branche locale.