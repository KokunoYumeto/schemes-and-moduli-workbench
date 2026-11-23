"""Independent finite certificate for the section-space calculation in paper 2.

No import from the original certificate. Truncated power series are sets of
exponents over F_2; the local unit is solved coefficientwise from
v+v^2+...+v^8=q. We then perform column reduction in a target space of
principal parts, with largest pivots. The original uses iterative inversion
and smallest-pivot row reduction. This program uses only Python's library.
"""
from math import comb
import json
PREC=8

def mul(a,b):
 out=set()
 for i in a:
  for j in b:
   if i+j<=PREC:
    if i+j in out:out.remove(i+j)
    else:out.add(i+j)
 return out

def power(a,n):
 out={0}
 for _ in range(n):out=mul(out,a)
 return out

v=set()
for n in range(1,PREC+1):
 tail=set()
 for j in range(2,9):tail ^= power(v,j)
 c=(1 if n==1 else 0) ^ (1 if n in tail else 0)
 if c:v.add(n)
u={0}^v
assert power(u,8)^power(u,7)=={1}
parts=[]
for i in range(3):
 a,b=6-i,9+2*i
 variables=[(j,r,s) for j in range(a+1) for s in range(2)
            for r in range(max(0,(2*b+7*a-j-15*s)//2+1))]
 columns=[];coords=set()
 for j,r,s in variables:
  column=set()
  for h in range(j+1):
   if comb(j,h)%2:
    for k in power(u,r+8*s):
     exp=2*b+7*h-j-2*r-15*s+15*k
     if exp<0:column.add((h,exp))
  columns.append(column);coords |= column
 pivots={}
 for column in columns:
  column=set(column)
  while column:
   p=max(column)
   if p in pivots:column ^= pivots[p]
   else:pivots[p]=column;break
 rr=sum(2*(b+3*j)-6 for j in range(a+1))
 d=len(variables)-len(pivots)
 assert d==rr
 parts.append(dict(eigenspace=i,variables=len(variables),principal_parts=len(coords),rank=len(pivots),nullity=d,Riemann_Roch=rr))
assert [x['nullity'] for x in parts]==[210,186,160]
h0_Q=sum((d//2+1) for d in [2,6])
h1_Q_inverse=1
h1_O=7+2
m=sum(x['nullity'] for x in parts)
assert (h0_Q,h1_Q_inverse,h1_O,m)==(6,1,9,556)
out=dict(method=__doc__.strip(),series_unit_exponents=sorted(u),parts=parts,
         root_count=m,h0_L=h0_Q+m,h1_L_inverse=h1_Q_inverse,h1_OY=h1_O+m,
         note='Finite coefficient check only. Smoothness, ampleness and all-degree cohomology require the proofs in the paper.')
print(json.dumps(out,indent=2))
