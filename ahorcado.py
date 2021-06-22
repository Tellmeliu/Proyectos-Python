
#%%
import random 

AHORCADO = ['''
       _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___         ''', '''
       _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___         ''', '''
       _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___         ''','''
       _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___         ''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___         ''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___         ''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___         ''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
    _|___         ''','''
''']

PALABRAS = [
    'principio',
    'dinero',
    'wels',
    'sitio',
    'tiempo',
    'silencio',
    'vino',
    'gente'
]

def random_word():
	x = random.randint(0,len(PALABRAS)-1)
	return PALABRAS[x]

def show_board(hidden_word, tries):
	print(AHORCADO[tries])
	print('')
	print(hidden_word)
	print('----* ----* ----* ----* ----* ----* ----*')

def run():
	pal = random_word()
	hidden_word = ['-']*len(pal)
	tries = 0

	while True:
		show_board(hidden_word,tries)
		current_letter = str(input('Escribe una letra: '))

		letter_indexes = []
		for x in range(len(pal)):
			if pal[x] == current_letter:
				letter_indexes.append(x)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 7:
				show_board(hidden_word,tries)
				print('')
				print('PERDISTE!!! La palabra correcta era: ',format(pal))
				break
		else:
			for x in letter_indexes:
				hidden_word[x] = current_letter

			letter_indexes = []

		try:
			hidden_word.index('-')
		except ValueError:
			print('')
			print('¡FELICIDADES GANASTE =D! La palabra es: ',format(pal))
			break

if __name__ == '__main__':
	print('EL JUEGO DEL AHORCADO')
	run()