mysql> select * from etudiant
    -> where age = (select min(age) from etudiant)
    -> ;