def primo(k):
	i=2
	while i<k:
		if k%i ==0:
			return False
		else:
			i+=1
	return True
def maior_primo(n):
	p = i =1
	while(i<=n):
		if primo(i):
			p=i
			i+=1
		else:
			i+=1
	return p
	
	
def vogal(l):
	if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
		return True
	elif l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
		return True
	else:
		return False