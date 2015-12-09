from linkedQFile import LinkedQ





class ParentNode:
    def __init__(self, kodordlista, parent = None):
    	self.kodordlista = kodordlista
    	self.avstand = berakna_avstand(kodordlista)

q = LinkedQ()

def main(kodordlista,avstandet):
	a = ParentNode(kodordlista)
	q.enqueue(a)
	found = False
	if berakna_avstand(kodordlista)>=avstandet:
		print("Hammingsavståndet av kodordlistan är redan större än eller lika med avståndet du angett.")
		return
	while not found:
		nod = q.dequeue()
		found = makechildren(nod,avstandet)

def berakna_avstand(kodordlista):
	m = len(kodordlista[0])
	n = len(kodordlista)
	lala=0
	d = len(kodordlista[0])

	for i in range(n):
		for j in range(i+1,n):
			lala=0
			for k in range(m):
				if kodordlista[i][k] != kodordlista[j][k]:
					lala +=1
			if lala<d:
				d=lala
	return d

def makechildren(node,avstandet):
	a = len(node.kodordlista)
	kombinationer = []
	barn = []
	for i in range(1,(2**a)-1):
		b=bin(i).split('b')[1].zfill(a)
		kombinationer.append(str(b))
	for j in kombinationer:
		barn = []
		for k in range(a):
			barn.append(node.kodordlista[k] +j[k])
		nodeny = ParentNode(barn, node)
		#if nodeny.avstand > node.avstand:
		q.enqueue(nodeny)
		if nodeny.avstand >= avstandet:
			print(nodeny.kodordlista)

			return True
	return False
		
main(["001","111","110", "000"],4)
main(["001","111","110", "000"],5)
	

