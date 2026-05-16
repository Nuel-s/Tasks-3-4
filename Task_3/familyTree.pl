% GRANDPARENTS
male(reuben).     
female(lily).
male(benjamin).      
female(grace).

% PARENTS
male(joseph).     
male(john).     
female(sally).
female(alpina).

% CHILDREN
male(victor). 
male(evans).
male(collins).       
female(linet).
female(oprah).

% PARENTS FACT DEFINITION 
parent(reuben, joseph).
parent(lily, joseph).
parent(reuben, john).
parent(lily, john).

parent(benjamin, sally).
parent(grace, sally).
parent(benjamin, alpina).
parent(grace, alpina).

parent(joseph, victor).
parent(sally, victor).
parent(joseph, evans).
parent(sally, evans).
parent(joseph, linet).
parent(sally, linet).

parent(john, collins).
parent(john, oprah).

% DEFINING RULES 
father(X, Y):- 
    male(X),
    parent(X, Y).

mother(X, Y):-
    female(X),
    parent(X, Y).
    
sibling(X, Y):-
    parent(P, X),
    parent(P, Y),
    X \= Y.

brother(X, Y):-
    male(X),
    sibling(X, Y).

sister(X, Y):-
    female(X),
    sibling(X, Y).

uncle(X, Y):-
    parent(P, Y),
    brother(X, P).

aunt(X, Y):-
    parent(P, Y),
    sister(X, P).

cousin(X, Y)      :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY).

grandparent(X, Z):-
    parent(X, Y),
    parent(Y, Z).

grandfather(X, Z):-
    male(X),
    grandparent(X, Z).

grandmother(X, Z):-
    female(X),
    grandparent(X, Z).

grandchild(X, Z):-
    grandparent(Z, X).