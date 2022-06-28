from selenium.webdriver.common.keys import Keys
from random import choice, randint
from selenium import webdriver
from time import sleep

class Instagram_ComentBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(randint(5, 6))

        caixa_usuário = driver.find_element_by_xpath('//input[@name="username"]')
        caixa_usuário.click() # Clica na caixa "usuário".
        caixa_usuário.clear() # Limpa a caixa, caso haja algo.
        caixa_usuário.send_keys(self.username) # Digita o usuário informada.
        
        caixa_senha = driver.find_element_by_xpath('//input[@name="password"]')
        caixa_senha.click() # Clica na caixa "password"
        caixa_senha.clear() # Limpa a caixa, caso haja algo.
        caixa_senha.send_keys(self.password) # Digita a senha informada.
        sleep(randint(2, 4))
        caixa_senha.send_keys(Keys.RETURN) # Aperta o botão "Enter".
        sleep(randint(4, 6)) # Aguarda alguns segundos antes de iniciar a pŕixima etapa. 

        self.comentário_na_postagem()

    @staticmethod
    def simulação_de_digitação(frase, onde_digitar): # Faz a digitação letra por letra.
        for letra in frase:
            onde_digitar.send_keys(letra)
            sleep(randint(4, 9) / 30)        

    def comentário_na_postagem(self):
        driver = self.driver
        sleep(randint(3, 5))
        link_postagem = str(input('Insira o link da postagem: '))
        driver.get(f'{link_postagem}') # Adicione o link da postagem que deseja comentar. 
        
        comentários = ['1', '2', '4'] # ADICIONE AQUI A SUA LISTA DE COMENTÁRIOS.
        
        num_comentários = int(input('Digite o número de comentários que deseja realizar: '))

        for c in range(num_comentários): # Delimita o número de comentários. 
            driver.find_element_by_class_name('Ypffh').click() # Clica no campo "Comentário"
            caixa_comentario = driver.find_element_by_class_name('Ypffh')

            sleep(randint(3, 7))

            self.simulação_de_digitação(choice(comentários), caixa_comentario) # Digita o comentário no campo
            sleep(randint(3, 6))

            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click() # Publica a postagem.
            sleep(randint(30, 60))
            print(f'Número de comentários postados: {c}') 

Instagram_ComentBot = Instagram_ComentBot('username', 'password') # Adicione aqui o seu usuário e senha.
Instagram_ComentBot.login()
