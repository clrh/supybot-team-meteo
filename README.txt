Displays data from a csv file to the team about its developments metrics.

$ cat metrics.ini
date,12/9/2014
heure,16:59:1
points engagés,14
points bonus,0
stories terminées,2
points terminés,3
demandes HL,45
48h,
urgent,3
haut,7
à intégrer,3
à tester,1
à rt,2
à documenter,1

> hlstat
45 en HL: 3 urgent(s), 7 haut(s)

> devstat
14 points engagés dont 0 points bonus, 3 points terminés de 2 stories

> wtdn
3 à intégrer, 1 à tester, 2 à rt, 1 à documenter

Memo for testing:
$ supybot-test --plugins-dir=..
