% A simple family (nuclear family)
male(joseph).
female(sally).
male(victor).
male(evans).
female(linet).

% This means joseph is the parent of victor. parent(X, Y), X is parent of Y
parent(joseph, victor).
parent(sally, victor).

parent(joseph, evans).
parent(sally, evans).

parent(joseph, linet).
parent(sally, linet).


% rules, we can define relationships this way
father(X, Y):- 
    male(X), 
    parent(X, Y).

mother(X, Y):-
    female(X),
    parent(X, Y).

sibling(X, Y):-
    parent(P, X),
    parent(P, Y),
    X \= Y. % This ensures someone cannot be their own sibling