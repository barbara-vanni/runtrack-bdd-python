mysql> select * from etudiant
    -> where age = (select max(age) from etudiant)
    -> ;