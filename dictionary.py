#	Dictionary
'''d1=dict()
print(d1,type(d1))
d2={1:123,2:456,2:100,3:123}
print(d2)
d3={'salom':True,False:1,100:'Hayr',3.1415:0}
print(d3)

print(d3['salom'])
print(d3.get('Salom'))

print(d3.keys())
print(d3.values())
print(d3.items())
d4=d3.copy()
print(d4)
t=d4.pop('salom')
print(d4,t)'''

d1={10:100,2:200,30:400}
d2={4:100,2:500}
d1.update(d2)
d1['alvido']=404
print(d1)
print(d1)
