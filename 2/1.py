def h(i):return"".join(list(i[::-1]));;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
c=h("ZYXWVUTSRQPONMLKJIHGFEDCBA"[::-1])[::-1];d=h(h('CSYJSYRHERSXLIVJPEK337'));e=4;;;;;;;;;;;;;;;;;
def f(a,b):return "".join([z if z.upper()not in c else c[(c.index(z.upper())+b)%len(c)]for z in a])
g=input("Enter correct key: ");;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
if g.__eq__(f(d,len(c)-e)):print("Yes! You found the right flag!");;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
else:print("Well, try again!");;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;